import jwt
import datetime
from app import app
from auth.config import Config



def encode_auth_token( user_id :int, secret :str ) -> str:
    expiry = datetime.datetime.utcnow() + datetime.timedelta( seconds=Config.TOKEN_VALIDITY )
    payload = {
        'exp': expiry,
        'iat': datetime.datetime.utcnow(),
        'sub': user_id,
        'secret': secret,
        'expiry': expiry.strftime('%s')
    }
    return jwt.encode(
        payload,
        app.secret_key,
        algorithm='HS256'
    )


def decode_auth_token( token :str ) -> dict:
    try:
        payload = jwt.decode( token, app.secret_key, algorithms='HS256' )
    except jwt.ExpiredSignatureError:
        raise Exception('Token expired.')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token.')
    return {
        'user_id': payload['sub'],
        'secret': payload['secret'],
        'expiry': payload['expiry']
    }
