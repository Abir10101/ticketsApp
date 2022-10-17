import os
from dotenv import load_dotenv


class Config:
    # Database configuration
    DB_HOST = os.environ.get('DB_HOST') or 'sql8.freemysqlhosting.net'
    DB_USER = os.environ.get('DB_USER') or 'sql8527240'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or '7eejrj5UeH'
    DB_NAME = os.environ.get('DB_NAME') or 'sql8527240'
    # Secret Key for application
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess'
