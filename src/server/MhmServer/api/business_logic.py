from MhmServer.database import db
from geoalchemy2 import functions as geo_func
import json

class BusinessLogic():

    @classmethod
    def get_locations(cls, location):
        locs = db.session.query(location).all()
        return cls.to_geojson(locs)

    # https://tools.ietf.org/html/rfc7946
    @classmethod
    def to_geojson(cls, locs, props={}):
        response = {}
        response['type'] = 'FeatureCollection'
        response['features'] = []
        for i in range(0, len(locs)):
            loc_dict = {}
            loc_dict['type'] = 'Feature'
            # omg I stored the order of lat/long wrong? jfc
            # stupid fix until I reingest the location data
            geo = json.loads(db.session.scalar(geo_func.ST_AsGeoJSON(locs[i].point)))
            geo['coordinates'][0], geo['coordinates'][1] = geo['coordinates'][1], geo['coordinates'][0]
            loc_dict['geometry'] = geo
            loc_dict['properties'] = {}
            loc_dict['properties']['name'] = locs[i].named_location
            loc_dict['properties']['elevation'] = locs[i].elevation
            loc_dict['properties']['domain'] = locs[i].domain
            if props:
                for key in props.keys():
                    loc_dict['properties'][key] = props[key][i]
            response['features'].append(loc_dict)

        return response

    @classmethod
    def get_leaderboards(cls, laboratory, scientist, sub_sample):
        response = {}
        response['byScientist'] = cls.__sum_sub_sample_individual_count(sub_sample, scientist)
        response['byLaboratory'] = cls.__sum_sub_sample_individual_count(sub_sample, laboratory)
        return response
        

    @classmethod
    def __sum_sub_sample_individual_count(cls, sub_sample, join_model):
        return db.session.query(
            join_model.id,
            join_model.name,
            db.func.sum(sub_sample.individual_count)
            .label('grouped_identifications')) \
        .join(join_model) \
        .group_by(join_model.name, join_model.id) \
        .order_by(db.desc('grouped_identifications')) \
        .all()

    @classmethod
    def get_genera(cls, specimen):
        unique_genera = db.session.query(specimen.genus) \
        .distinct(specimen.genus) \
        .filter(specimen.genus != '') \
        .all()
        genera_list = list(list(zip(*unique_genera))[0])
        response = []
        for i in range(0, len(genera_list)):
            genus_dict = {}
            genus_dict['id'] = i
            genus_dict['name'] = genera_list[i]
            response.append(genus_dict)

        return response

    @classmethod
    def get_by_genus(cls, location, sample, specimen, sub_sample, genus):
        by_genus = db.session.query(
            location,
            db.func.sum(sub_sample.individual_count)
            .label('genus_count')) \
        .select_from(location) \
        .join(sample) \
        .join(sub_sample) \
        .join(specimen) \
        .filter(specimen.genus == genus) \
        .group_by(location) \
        .order_by(db.desc('genus_count')) \
        .all()

        locs, counts = list(zip(*by_genus))
        counts = {'count': counts}
        return cls.to_geojson(locs, counts)
