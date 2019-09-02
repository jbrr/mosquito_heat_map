from app import db
import datetime

class NlcdClass(db.Model):
    __tablename__ = 'nlcd_class'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.now)
    sub_samples = db.relationship('Location', cascade='all,delete-orphan', backref='NlcdClass')

    def __repr__(self):
        return '<id {}>'.format(self.id)