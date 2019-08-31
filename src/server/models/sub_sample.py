from app import db

class SubSample(db.Model):
	__tablename__ = 'sub_sample'

	id = db.Column(db.Integer, primary_key=True)
	sample_id = db.Column(db.Integer, db.ForeignKey('sample.id'))
	identified_by = db.Column(db.String())
	identified_by_lab = db.Column(db.String())
	specimen_id = db.Column(db.Integer, db.ForeignKey('specimen.id'))

	def __init__(self, sample_id, identified_by, identified_by_lab, specimen_id):
		self.sample_id = sample_id
		self.identified_by = identified_by
		self.identified_by_lab = identified_by_lab
		self.specimen_id = specimen_id

	def __repr__(self):
		return '<id {}>'.format(self.id)