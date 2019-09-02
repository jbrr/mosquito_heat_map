from app import db
import datetime

class Scientist(db.Model):
    __tablename__ = 'scientist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.now)
    sub_samples = db.relationship('SubSample', cascade='all,delete-orphan', backref='scientist')

    def __repr__(self):
        return '<id {}>'.format(self.id)