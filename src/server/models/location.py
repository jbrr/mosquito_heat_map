from app import db

class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.String())
    domain = db.Column(db.String())
    named_location = db.Column(db.String())
    latitude = db.Column(db.String())
    longitude = db.Column(db.String())
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    samples = db.relationship('Sample')

    def __init__(self, site_id, domain, named_location, latitude, longitude, created_at, updated_at, samples):
        self.site_id = site_id
        self.domain = domain
        self.named_location = named_location
        self.latitude = latitude
        self.longitude = longitude
        self.created_at = created_at
        self.updated_at = updated_at
        self.samples = samples

    def __repr__(self):
        return '<id {}>'.format(self.id)