import psycopg2
import os
from urllib.parse import urlparse


def db_connection():
    result = urlparse('postgres://ahctpxqu:P2QBzx8mTAtPdzBKVloYGpGiATZuA2Rh@jelani.db.elephantsql.com/ahctpxqu')
    username = result.username
    password = result.password
    database = result.path[1:]
    hostname = result.hostname
    port = result.port
    con = psycopg2.connect(
        database = database,
        user = username,
        password = password,
        host = hostname,
        port = port
    )
    # uri = os.environ.get("DB_URI") or 'postgres://ahctpxqu:P2QBzx8mTAtPdzBKVloYGpGiATZuA2Rh@jelani.db.elephantsql.com/ahctpxqu'
    # con = psycopg2.connect(uri)
    return con
