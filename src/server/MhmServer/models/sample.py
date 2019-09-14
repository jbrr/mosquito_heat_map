from MhmServer.database import (Column, DateTime, ForeignKey, func, Integer, Model, relationship)
import datetime

class Sample(Model):
    __tablename__ = 'sample'

    id = Column(Integer, primary_key=True)
    set_date = Column(DateTime())
    collect_date = Column(DateTime())
    location_id = Column(Integer, ForeignKey('location.id'))
    sub_samples = relationship('SubSample', cascade='all,delete-orphan', backref='sample')
    created_at = Column(DateTime(), default=func.now())
    updated_at = Column(DateTime(), onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<id {}>'.format(self.id)