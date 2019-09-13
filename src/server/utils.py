from app import db
from geoalchemy2 import functions as geo_func
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
            geo = json.loads(db.session.scalar(geo_func.ST_AsGeoJSON(loc.point)))
            geo['coordinates'][0], geo['coordinates'][1] = geo['coordinates'][1], geo['coordinates'][0]
            loc_dict['geometry'] = geo
            loc_dict['properties'] = {}
            loc_dict['properties']['name'] = loc.named_location
            loc_dict['properties']['elevation'] = loc.elevation
            loc_dict['properties']['domain'] = loc.domain
            response['features'].append(loc_dict)

        return response

    @classmethod
    def get_leaderboards(cls, models):
        response = {}
        response['byScientist'] = cls.__sum_sub_sample_individual_count(models['sub_sample'], models['scientist'])
        response['byLaboratory'] = cls.__sum_sub_sample_individual_count(models['sub_sample'], models['laboratory'])
        return response
        

    @classmethod
    def __sum_sub_sample_individual_count(cls, sub_sample, join_model):
        return db.session.query(
            join_model.name,
            db.func.sum(sub_sample.individual_count)
            .label('grouped_identifications')) \
        .join(join_model) \
        .group_by(join_model.name) \
        .order_by(db.desc('grouped_identifications')) \
        .all()
