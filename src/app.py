import os
import logging
from .config import *

from flask import Flask
from dotenv import load_dotenv
from flasgger import Swagger
from flask_cors import CORS

from .docs.swagger import template,swagger_config
from .api.scraper_api import scraper_route

load_dotenv()

logging.getLogger('flask_cors').level = logging.DEBUG


def create_app():
    """
    Main App
    """
    app = Flask(__name__)

    if os.environ.get("FLASK_ENV")=="production":
        app.config.from_object(ProductionConfig)
    elif os.environ.get("FLASK_ENV")=="development":
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(TestingConfig)

    # CORS(app, resources=r'/api/*')
    
    # Register domain bluprints
    app.register_blueprint(scraper_route)

    Swagger(app, config=swagger_config, template=template)
    
    return app

