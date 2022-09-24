import pymysql
import os


def db_connection():
    con = pymysql.connect(  host="sql6.freemysqlhosting.net",
                            user="sql6521869",
                            password="VtjDmWW1ed",
                            database="sql6521869" )
    return con
