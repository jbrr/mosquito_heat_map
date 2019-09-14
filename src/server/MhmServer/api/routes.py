from flask import Blueprint, jsonify

from MhmServer.api.business_logic import BusinessLogic
from MhmServer.models.laboratory import Laboratory
from MhmServer.models.location import Location
from MhmServer.models.nlcd_class import NlcdClass
from MhmServer.models.sample import Sample
from MhmServer.models.scientist import Scientist
from MhmServer.models.specimen import Specimen
from MhmServer.models.sub_sample import SubSample

blueprint = Blueprint('routes', __name__, url_prefix='/api/v0')

@blueprint.route('/locations')
def get_locations():
    locs = db.session.query(Location).all()
    geojson = Utils.to_geojson(locs)
    return jsonify(geojson)

@blueprint.route('/leaderboards')
def get_leaderboards():
    leaderboards = Utils.get_leaderboards(Laboratory, Scientist, SubSample)
    return jsonify(leaderboards)