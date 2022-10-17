from flask import Flask
from app.config import Config
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.secret_key = Config.SECRET_KEY

from app import logger
from app import routes
