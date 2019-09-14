from MhmServer.database import (Column, DateTime, func, Integer, Model, relationship, String)
import datetime

class Specimen(Model):
    __tablename__ = 'specimen'

    id = Column(Integer, primary_key=True)
    kingdom = Column(String())
    phylum = Column(String())
    # class is a reserved keyword
    tax_class = Column('class', String())
    order = Column(String())
    family = Column(String())
    subfamily = Column(String())
    tribe = Column(String())
    genus = Column(String())
    subgenus = Column(String())
    species = Column(String())
    sub_samples = relationship('SubSample', cascade='all,delete-orphan', backref='specimen')
    created_at = Column(DateTime(), default=func.now())
    updated_at = Column(DateTime(), onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<id {}>'.format(self.id)