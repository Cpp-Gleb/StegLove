import os
import uuid
import subprocess
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template_string

load_dotenv()


class App():
    def __init__(self):
        self.app = Flask(__name__, static_folder='static')
        self.app.secret_key = os.getenv('KEY')
        self.routes()
        self.errors()

    def run(self, **kwargs):
        self.app.run(**kwargs)

    def errors(self):
        file = self.render('error')

        @self.app.errorhandler(400)
        def bad_req(e):
            file = self.render('index')
            return render_template_string(file), 400
        
        @self.app.errorhandler(403)
        def restricted(e):
            return render_template_string(file, title='404 - Not Found'), 404
        
        @self.app.errorhandler(404)
        def page_not_found(e):
            return render_template_string(file, title='404 - Not Found'), 404
        
        @self.app.errorhandler(405)
        def not_allowed(e):
            return render_template_string(file, title='404 - Not Found'), 405
        
        @self.app.errorhandler(500)
        def server_error(e):
            return render_template_string(file, title='500 - Server Error'), 500

    def save(self, file):
        data = bytes.fromhex(file)
        name = str(uuid.uuid4().hex)

        current_datetime = datetime.now()
        date = current_datetime.strftime("%Y-%m-%d_%H-%M")
        path = f'temp/{name}_{date}'

        with open(path, 'wb') as file:
            file.write(data)

        return path

    def analyze(self, tool, path):
        try:
            full_path = os.path.abspath(path)
            result = subprocess.run([tool, full_path], capture_output=True, text=True)
            output = str(result.stdout)

            try:
                response = {
                    'status': 'ok',
                    'tool': tool,
                    'result': output
                }
            except:
                response = {
                    'status': 'error',
                    'tool': tool
                }

        except:
            response = {
                'status': 'error',
                'tool': tool
            }

        finally:
            try:
                os.remove(full_path)
            except:
                pass

        return response

    def render(self, template):
        with open(f'templates/{template}.html', 'r', encoding='utf8') as f: file = f.read()
        return file

    def routes(self):
        @self.app.route('/')
        def home():
            file = self.render('index')
            tool = str(request.args.get('tool', default='exiftool'))
            return render_template_string(file, tool=tool)
        
        @self.app.route('/result', methods=['POST'])
        def result():
            file = self.render('result')
            result = str(request.json.get('result'))
            return render_template_string(file, result=result)

        @self.app.route('/api/<tool>', methods=['POST'])
        def api(tool):
            try:
                tool = str(tool)
                data = request.json
                file = data.get('file')
                path = self.save(file)
                result = self.analyze(tool, path)
            except:
                result = {
                    'status': 'error',
                    'tool': tool
                }
            finally:
                return jsonify(result)



if __name__ == '__main__':
    app = App()
    app.run(host='0.0.0.0', port=5000, debug=False)
