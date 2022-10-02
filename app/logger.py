import os
from app import app
import logging



if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = logging.handlers.RotatingFileHandler(
            'logs/microblog.log',
            maxBytes=10240,
            backupCount=10
        )
    file_handler.setFormatter(
            logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
            )
        )
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')


def log( message :str ):
    app.logger.setLevel(logging.INFO)
    app.logger.info( message )
