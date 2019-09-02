from app import db
import datetime

class Specimen(db.Model):
    __tablename__ = 'specimen'

    id = db.Column(db.Integer, primary_key=True)
    kingdom = db.Column(db.String())
    phylum = db.Column(db.String())
    # class is a reserved keyword
    tax_class = db.Column('class', db.String())
    order = db.Column(db.String())
    family = db.Column(db.String())
    subfamily = db.Column(db.String())
    tribe = db.Column(db.String())
    genus = db.Column(db.String())
    subgenus = db.Column(db.String())
    species = db.Column(db.String())
    sub_samples = db.relationship('SubSample', cascade='all,delete-orphan', backref='specimen')
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<id {}>'.format(self.id)