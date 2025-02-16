import asyncio

from flask import Flask
from flask_cors import CORS
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from core.routes import Routes
from core.config import config
from core.utils import app_utils
from core.handlers import Errors


class App:
    def __init__(self):
        self.app = Flask(__name__, static_folder='static')

        self.app.config['SESSION_COOKIE_SECURE'] = True
        self.app.secret_key = config.app_key.get_secret_value()

        CORS(self.app)
        Routes(self.app)
        Errors(self.app)

    async def run(self, **kwargs):
        await app_utils.remove_pycache()
        self.app.run(**kwargs)


if __name__ == '__main__':
    app = App()
    asyncio.run(app.run(host='0.0.0.0', port=5000, debug=False))
