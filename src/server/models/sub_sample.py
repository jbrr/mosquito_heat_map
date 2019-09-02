from app import db
import datetime

class SubSample(db.Model):
    __tablename__ = 'sub_sample'

    id = db.Column(db.Integer, primary_key=True)
    sample_id = db.Column(db.Integer, db.ForeignKey('sample.id'), nullable=False)
    identified_by = db.Column(db.Integer, db.ForeignKey('scientist.id'))
    identified_by_lab = db.Column(db.Integer, db.ForeignKey('laboratory.id'))
    individual_count = db.Column(db.Integer)
    specimen_id = db.Column(db.Integer, db.ForeignKey('specimen.id'))
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<id {}>'.format(self.id)