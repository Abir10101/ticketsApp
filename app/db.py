import psycopg2
import os


def db_connection():
    uri = os.environ.get("DB_URI") or 'postgres://ahctpxqu:P2QBzx8mTAtPdzBKVloYGpGiATZuA2Rh@jelani.db.elephantsql.com/ahctpxqu'
    con = psycopg2.connect(uri)
    return con
