from flask import Flask
from flask import jsonify
import os

from MhmServer.extensions import (db, cors)
from MhmServer.api import routes
from MhmServer.models.laboratory import Laboratory
from MhmServer.models.location import Location
from MhmServer.models.nlcd_class import NlcdClass
from MhmServer.models.sample import Sample
from MhmServer.models.scientist import Scientist
from MhmServer.models.specimen import Specimen
from MhmServer.models.sub_sample import SubSample

def create_app(config_object=os.environ['APP_SETTINGS']):
    app = Flask('mhm')
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)

    return app

def register_extensions(app):
    db.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    return None

def register_blueprints(app):
    app.register_blueprint(routes.blueprint)