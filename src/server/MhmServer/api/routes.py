from flask import Blueprint, jsonify

from MhmServer.database import db
from MhmServer.api.business_logic import BusinessLogic
from MhmServer.models import (Laboratory, Location, Scientist, SubSample)

blueprint = Blueprint('routes', __name__, url_prefix='/api/v0')


@blueprint.route('/locations')
def get_locations():
    locs = db.session.query(Location).all()
    geojson = BusinessLogic.to_geojson(locs)
    return jsonify(geojson)


@blueprint.route('/leaderboards')
def get_leaderboards():
    leaderboards = BusinessLogic.get_leaderboards(Laboratory, Scientist, SubSample)
    return jsonify(leaderboards)