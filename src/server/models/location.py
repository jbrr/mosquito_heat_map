from app import db
from geoalchemy2 import Geometry, functions
import datetime

class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.String())
    domain = db.Column(db.String())
    named_location = db.Column(db.String(), unique=True)
    elevation = db.Column(db.Float)
    point = db.Column(Geometry('POINT', srid=4326))
    nlcd_class_id = db.Column(db.ForeignKey('nlcd_class.id'))
    county = db.Column(db.String())
    state = db.Column(db.String())
    country = db.Column(db.String())
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.now)
    samples = db.relationship('Sample', cascade='all,delete-orphan', backref='location')

    def __repr__(self):
        return '<id {}>'.format(self.id)
