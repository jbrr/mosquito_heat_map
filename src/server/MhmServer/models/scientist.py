from MhmServer.database import (Column, DateTime, func, Integer, Model, relationship, String)
import datetime

class Scientist(Model):
    __tablename__ = 'scientist'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    created_at = Column(DateTime(), default=func.now())
    updated_at = Column(DateTime(), onupdate=datetime.datetime.now)
    sub_samples = relationship('SubSample', cascade='all,delete-orphan', backref='scientist')

    def __repr__(self):
        return '<id {}>'.format(self.id)