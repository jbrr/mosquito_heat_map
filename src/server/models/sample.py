from app import db
import datetime

class Sample(db.Model):
    __tablename__ = 'sample'

    id = db.Column(db.Integer, primary_key=True)
    set_date = db.Column(db.DateTime())
    collect_date = db.Column(db.DateTime())
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    sub_samples = db.relationship('SubSample', cascade='all,delete-orphan', backref='sample')
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<id {}>'.format(self.id)