import os
from dotenv import load_dotenv


class Config:
    # Database configuration
    DB_HOST = os.environ.get('DB_HOST') or 'sql6.freemysqlhosting.net'
    DB_USER = os.environ.get('DB_USER') or 'sql6522130'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'JlJf8vElrz'
    DB_NAME = os.environ.get('DB_NAME') or 'sql6522130'
    # Secret Key for application
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess'
