from flask import Blueprint, jsonify, request

from MhmServer.database import db
from MhmServer.api.business_logic import BusinessLogic
from MhmServer.models import (Laboratory, Location, Sample, Scientist, Specimen, SubSample)

blueprint = Blueprint('routes', __name__, url_prefix='/api/v0')


@blueprint.route('/locations')
def get_locations():
    geojson = BusinessLogic.get_locations(Location)
    return jsonify(geojson)


@blueprint.route('/leaderboards')
def get_leaderboards():
    leaderboards = BusinessLogic.get_leaderboards(Laboratory, Scientist, SubSample)
    return jsonify(leaderboards)

@blueprint.route('/genera')
def get_genera():
    genera = BusinessLogic.get_genera(Specimen)
    return jsonify(genera)

@blueprint.route('/genera/<name>')
def get_genus_distribution(name):
    genus_distribution = BusinessLogic.get_by_genus(Location, Sample, Specimen, SubSample, name)
    return jsonify(genus_distribution)