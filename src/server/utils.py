from app import db
from geoalchemy2 import functions as func
import json

class Utils():

    # https://tools.ietf.org/html/rfc7946
    @classmethod
    def to_geojson(cls, locs):
        response = {}
        response['type'] = 'FeatureCollection'
        response['features'] = []
        for loc in locs:
            loc_dict = {}
            loc_dict['type'] = 'Feature'
            # omg I stored the order of lat/long wrong? jfc
            # stupid fix until I reingest the location data
            geo = json.loads(db.session.scalar(func.ST_AsGeoJSON(loc.point)))
            geo['coordinates'][0], geo['coordinates'][1] = geo['coordinates'][1], geo['coordinates'][0]
            loc_dict['geometry'] = geo
            loc_dict['properties'] = {}
            loc_dict['properties']['name'] = loc.named_location
            loc_dict['properties']['elevation'] = loc.elevation
            loc_dict['properties']['domain'] = loc.domain
            response['features'].append(loc_dict)

        return response