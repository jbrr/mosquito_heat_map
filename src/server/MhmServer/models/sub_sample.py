from MhmServer.database import (Column, DateTime, ForeignKey, func, Integer, Model)
import datetime


class SubSample(Model):
    __tablename__ = 'sub_sample'

    id = Column(Integer, primary_key=True)
    sample_id = Column(Integer, ForeignKey('sample.id'), nullable=False)
    identified_by = Column(Integer, ForeignKey('scientist.id'))
    identified_by_lab = Column(Integer, ForeignKey('laboratory.id'))
    individual_count = Column(Integer)
    specimen_id = Column(Integer, ForeignKey('specimen.id'))
    created_at = Column(DateTime(), default=func.now())
    updated_at = Column(DateTime(), onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<id {}>'.format(self.id)