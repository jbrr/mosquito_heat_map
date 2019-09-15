from flask import Flask
import os

from MhmServer import commands
from MhmServer.extensions import (db, cors, migrate)
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
    register_shellcontext(app)
    register_commands(app)

    return app


def register_extensions(app):
    db.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    migrate.init_app(app, db, 'src/server/MhmServer/migrations')

    return None


def register_blueprints(app):
    app.register_blueprint(routes.blueprint)


def register_shellcontext(app):

    def shell_context():
        return dict(db=db, app=app, Laboratory=Laboratory, Location=Location, NlcdClass=NlcdClass, Sample=Sample,
                    Scientist=Scientist, Specimen=Specimen, SubSample=SubSample)

    app.shell_context_processor(shell_context)


def register_commands(app):
    app.cli.add_command(commands.ingestiddata)
    app.cli.add_command(commands.ingestlocationdata)