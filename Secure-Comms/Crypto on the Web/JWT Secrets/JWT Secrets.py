import base64
import json
import jwt # note this is the PyJWT module, not python-jwt

SECRET_KEY = 'secret' #key from PyJWT https://pyjwt.readthedocs.io/en/stable/


def create_session(username):
    encoded = jwt.encode({'username': username, 'admin': True}, SECRET_KEY, algorithm="HS256")
    return {"session": encoded.decode()}

token = create_session('admin')
print(token)
