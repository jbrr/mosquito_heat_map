from MhmServer.database import (Column, DateTime, func, Integer, Model, relationship, String)
import datetime


class NlcdClass(Model):
    __tablename__ = 'nlcd_class'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    created_at = Column(DateTime(), default=func.now())
    updated_at = Column(DateTime(), onupdate=datetime.datetime.now)
    sub_samples = relationship('Location', cascade='all,delete-orphan', backref='NlcdClass')

    def __repr__(self):
        return '<id {}>'.format(self.id)