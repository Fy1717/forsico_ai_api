import os
from functools import wraps
from flask import request, jsonify
import jwt
from app.models import create_log
from app import createApp

app = createApp()

SECRET_KEY = os.getenv('SECRET_KEY', "Bnxfm3x42ynnTUONOuE7gXCmb2oXYFzL")


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data['user_id']
        except Exception as e:
            create_log(0, str(e))
            
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
