from app import db

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
	sub_samples = db.relationship('SubSample')

	def __init__(self, kingdom, phylum, tax_class, order, family, subfamily, tribe, genus, subgenus, species):
		self.kingdom = kingdom
		self.phylum = phylum
		self.tax_class = tax_class
		self.order = order
		self.family = family
		self.subfamily = subfamily
		self.tribe = tribe
		self.genus = genus
		self.subgenus = subgenus
		self.species = species
		self.sub_samples = sub_samples

	def __repr__(self):
		return '<id {}>'.format(self.id)