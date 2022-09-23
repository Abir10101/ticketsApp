import psycopg2
import os


def db_connection():
    uri = os.environ.get("DB_URI") or 'postgres://abir101:ticketsAppdb@abir101.mysql.pythonanywhere-services.com/ticketsApp'
    con = psycopg2.connect(uri)
    return con
