import asyncio
from flask import render_template_string
from core.utils import app_utils


class Errors:
    def __init__(self, app):
        self.app = app
        self._set_errors()

    def _set_errors(self):
        file = asyncio.run(app_utils.render_template('error'))

        @self.app.errorhandler(400)
        async def bad_req(e):
            file = await app_utils.render_template('index')
            return render_template_string(file), 400
        
        @self.app.errorhandler(403)
        async def restricted(e):
            return render_template_string(file, title='404 - Not Found'), 404
        
        @self.app.errorhandler(404)
        async def page_not_found(e):
            return render_template_string(file, title='404 - Not Found'), 404
        
        @self.app.errorhandler(405)
        async def not_allowed(e):
            return render_template_string(file, title='404 - Not Found'), 405
        
        @self.app.errorhandler(500)
        async def server_error(e):
            return render_template_string(file, title='500 - Server Error'), 500
        