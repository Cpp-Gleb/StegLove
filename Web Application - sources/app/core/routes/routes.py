from flask import request, jsonify, \
    render_template_string, redirect

from core.utils import app_utils
from core.decorators import preprocess


class Routes:
    def __init__(self, app):
        self.app = app
        self._set_routes()

    def _set_routes(self):
        @self.app.route('/')
        @preprocess
        async def home():
            session = request.cookies.get('session')
            file = await app_utils.render_template('index')
            tool = str(request.args.get('tool', default='exiftool'))
            data = await app_utils.get_analyze_sessions(session)
            data = data if data else {}
            return render_template_string(file, tool=tool, data=data)
        
        @self.app.route('/result', methods=['POST'])
        @preprocess
        async def result():
            file = await app_utils.render_template('result')
            result = str(request.json.get('result'))
            result2 = str(request.json.get('result2'))
            return render_template_string(file, result=result, result2=result2)
        
        @self.app.route('/session/<analyze_id>')
        @preprocess
        async def session(analyze_id):
            session = request.cookies.get('session')
            if not await app_utils.check_file_analyze_session(session, analyze_id):
                return redirect('/')

            file = await app_utils.render_template('result')
            result, result2 = await app_utils.get_analyze_results(session, analyze_id)
            return render_template_string(file, result=result, result2=result2)

        @self.app.route('/api/<tool>', methods=['POST'])
        @preprocess
        async def api(tool):
            try:
                session = request.cookies.get('session')
                data = request.json
                file = data.get('file')
                path = await app_utils.save_file(file)
                result = await app_utils.analyze_file(tool, path)
                await app_utils.add_analyze_results(result, session)
            except:
                result = {
                    'status': 'error',
                    'tool': tool
                }
            finally:
                return jsonify(result)
