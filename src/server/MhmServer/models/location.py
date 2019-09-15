from MhmServer.database import (Column, DateTime, Float, ForeignKey, func, Integer, Model, String, relationship)
from geoalchemy2 import Geometry
import datetime


class Location(Model):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    site_id = Column(String())
    domain = Column(String())
    named_location = Column(String(), unique=True)
    elevation = Column(Float)
    point = Column(Geometry('POINT', srid=4326))
    nlcd_class_id = Column(ForeignKey('nlcd_class.id'))
    county = Column(String())
    state = Column(String())
    country = Column(String())
    created_at = Column(DateTime(), default=func.now())
    updated_at = Column(DateTime(), onupdate=datetime.datetime.now)
    samples = relationship('Sample', cascade='all,delete-orphan', backref='location')

    def __repr__(self):
        return '<id {}>'.format(self.id)
