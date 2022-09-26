import pymysql
from app.config import Config


def db_connection():
    try:
        con = pymysql.connect(  host = Config.DB_HOST,
                                user = Config.DB_USER,
                                password = Config.DB_PASSWORD,
                                database = Config.DB_NAME,
                                cursorclass = pymysql.cursors.DictCursor )
    except pymysql.err.DatabaseError:
        raise Exception('Cannot connect Database')
    return con
