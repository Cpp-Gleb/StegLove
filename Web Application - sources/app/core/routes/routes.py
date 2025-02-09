from flask import request, jsonify, \
    render_template_string

from core.utils import app_utils


class Routes:
    def __init__(self, app):
        self.app = app
        self._set_routes()

    def _set_routes(self):
        @self.app.route('/')
        async def home():
            file = await app_utils.render_template('index')
            tool = str(request.args.get('tool', default='exiftool'))
            return render_template_string(file, tool=tool)
        
        @self.app.route('/result', methods=['POST'])
        async def result():
            file = await app_utils.render_template('result')
            result = str(request.json.get('result'))
            result2 = str(request.json.get('result2'))
            return render_template_string(file, result=result, result2=result2)

        @self.app.route('/api/<tool>', methods=['POST'])
        async def api(tool):
            try:
                data = request.json
                file = data.get('file')
                path = await app_utils.save_file(file)
                result = await app_utils.analyze_file(tool, path)
            except Exception as e:
                result = {
                    'status': 'error',
                    'tool': tool
                }
            finally:
                return jsonify(result)
