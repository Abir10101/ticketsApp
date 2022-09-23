from flask_mysql_connector import MySQL
from app import app
import os


def db_connection():
    # uri = os.environ.get("DB_URI") or 'mysql://abir101:ticketsAppdb@abir101.mysql.pythonanywhere-services.com/abir$ticketsApp'
    app.config['MYSQL_USER'] = 'abir101'
    app.config['MYSQL_DATABASE'] = 'abir$ticketsApp'
    app.config['MYSQL_HOST'] = 'abir101.mysql.pythonanywhere-services.com'
    app.config['MYSQL_PASSWORD'] = 'ticketsAppdb'
    mysql = MySQL(app)
    return mysql.connection
