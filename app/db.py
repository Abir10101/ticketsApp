import pymysql
import os


def db_connection():
    # uri = os.environ.get("DB_URI") or 'mysql://abir101:ticketsAppdb@abir101.mysql.pythonanywhere-services.com/abir$ticketsApp'
    con = pymysql.connect(host="abir101.mysql.pythonanywhere-services.com",user="abir101",password="ticketsAppdb",database="abir$ticketsApp" )
    return con
