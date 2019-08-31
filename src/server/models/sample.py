from app import db

class Sample(db.Model):
	__tablename__ = 'sample'

	id = db.Column(db.Integer, primary_key=True)
	set_date = db.Column(db.DateTime())
	collect_date = db.Column(db.DateTime())
	location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
	sub_samples = db.relationship('SubSample')

	def __init__(self, set_date, collect_date, location_id, sub_samples):
		self.set_date = set_date
		self.collect_date = collect_date
		self.location_id = location_id
		self.sub_samples = sub_samples

	def __repr__(self):
		return '<id {}>'.format(self.id)