import datetime
import bcrypt
import secrets
from app.db import *
from auth import *



def register( username :str, password :str, name :str ) -> str:
    hashed = bcrypt.hashpw( password.encode(), bcrypt.gensalt() )
    secret = secrets.token_urlsafe(10)
    con = db_connection()
    cur = con.cursor()
    try:
        cur.execute(
            "INSERT INTO users (u_name, u_username, u_password, u_secret) VALUES ( %s, %s, %s, %s );",
            (name, username, hashed, secret)
        )
        user_id = con.insert_id()
        con.commit()
        token = encode_auth_token( user_id, secret )
    except pymysql.err.IntegrityError:
        con.rollback()
        raise Exception(f"Username {username} already exists")
    except Exception:
        con.rollback()
    finally:
        cur.close()
        con.close()
    return token


def login( username :str, password :str ) -> str:
    con = db_connection()
    cur = con.cursor()
    try:
        cur.execute(
            "SELECT id, u_name, u_password, u_secret FROM users WHERE u_username = %s;",
            (username)
        )
        user = cur.fetchone()
    except Exception as err:
        raise Exception(err)
    finally:
        cur.close()
        con.close()
    if user:
        if bcrypt.checkpw( password.encode(), user['u_password'].encode() ):
            token = encode_auth_token( user['id'], user['u_secret'] )
        else:
            raise Exception("Invalid Password")
    else:
        raise Exception("User does not exists")
    return token


def logout( token :str ) -> bool:
    user_id = decode_auth_token( token )['user_id']
    secret = secrets.token_urlsafe(10)
    con = db_connection()
    cur = con.cursor()
    try:
        cur.execute(
            "UPDATE users SET u_secret = %s WHERE id = %s;",
            (secret, user_id)
        )
        con.commit()
    except Exception as err:
        con.rollback()
        raise Exception(err)
    finally:
        cur.close()
        con.close()
    return True


def status( token :str ) -> str:
    decoded = decode_auth_token( token )
    user_id = decoded['user_id']
    token_secret = decoded['secret']
    token_exp = datetime.datetime.fromtimestamp( int(decoded['expiry']) )
    con = db_connection()
    cur = con.cursor()
    try:
        cur.execute(
            "SELECT u_secret FROM users WHERE id = %s;",
            (user_id)
        )
        user_secret = cur.fetchone()['u_secret']
        con.commit()
        # check if user has logged out
        if token_secret != user_secret:
            return False
    except Exception as err:
        raise Exception(err)
    finally:
        cur.close()
        con.close()
    # check if token expiry less than 30 min left
    if (token_exp - datetime.datetime.utcnow()) < datetime.timedelta( seconds=Config.TOKEN_REFRESH_RATE ):
        new_token = encode_auth_token( user_id, token_secret )
        return new_token
    else:
        return token
