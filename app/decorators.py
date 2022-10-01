from functools import wraps
from flask import request
import auth



def token_required(f):
    @wraps(f)
    def decorated( *args, **kwargs ):
        try:
            token = request.headers['Authorization'].split(" ")[1]
            details = auth.user.details( token )
            return f( details["user_id"], details["token"] )
        except KeyError as err:
            response = {
                "isOk": False,
                "status": 500,
                "message": "Auth Token Required!"
            }
            return response
        except Exception as err:
            response = {
                "isOk": False,
                "status": 500,
                "message": f"{err}"
            }
            return response
    return decorated
