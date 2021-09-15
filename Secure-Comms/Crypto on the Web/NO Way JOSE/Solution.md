Flag = crypto{The_Cryptographic_Doom_Principle}

Generate a new token Using none algorithm and set admin value to true as mentioned below

def create_session(username):
    encoded = jwt.encode({'username': username, 'admin': True}, SECRET_KEY, algorithm="none")
    return {"session": encoded.decode()}

Secret key will be empty, no need to worry

After generating the token, head to Cryptohack.org and in the play at section place it under token and click submit, u will obtain the flag