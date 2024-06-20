import jwt
import datetime

SECRET_KEY = 'your_secret_key'  

def generate_token():
    token = jwt.encode({
        'user': 'test_user',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, SECRET_KEY, algorithm="HS256")
    return token

print(generate_token())
