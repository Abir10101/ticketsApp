from functools import wraps
from flask import request
import auth



def token_required(f):
    @wraps(f)
    def decorated( *args, **kwargs ):
        token = request.headers['Authorization']
        try:
            details = auth.user.details( token )
            return f( details["user_id"], details["token"] )
        except Exception as err:
            response = {
                "isOk": False,
                "status": 500,
                "message": f"{err}"
            }
            return response
    return decorated
