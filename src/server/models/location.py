from app import db
import datetime

class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.String())
    domain = db.Column(db.String())
    named_location = db.Column(db.String())
    latitude = db.Column(db.String())
    longitude = db.Column(db.String())
    state = db.Column(db.String())
    country = db.Column(db.String(), server_default='US')
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.now)
    samples = db.relationship('Sample', cascade='all,delete-orphan', backref='location')

    def __repr__(self):
        return '<id {}>'.format(self.id)