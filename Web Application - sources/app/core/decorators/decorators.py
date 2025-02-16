from functools import wraps
from flask import request, make_response, jsonify, redirect

from core.utils import app_utils


class Decorators:
    def preprocess(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            response = await func(*args, **kwargs)
            session = request.cookies.get('session')

            if session is None or not await app_utils.check_session(session):
                if request.path != '/':
                    return redirect('/')
                    
                new_session = await app_utils.create_session(request.remote_addr)

                if isinstance(response, dict):
                    response = make_response(jsonify(response))
                elif isinstance(response, str):
                    response = make_response(response)

                response.set_cookie('session', new_session, secure=True, samesite='Lax', max_age=604800)

            return response

        return wrapper
