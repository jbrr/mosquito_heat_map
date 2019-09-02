import re
import csv

class NeonIngestor():
    def __init__(self, app, db, models, file_path):
        self.app = app
        self.db = db
        self.models = models
        self.file_path = file_path

    def ingest_identification_data(self):
        data = []
        session = self.db.session()
        with open(self.file_path) as f:
            reader = csv.DictReader(f)
            data = [r for r in reader]

        for r in data:
            try:
                loc = self.get_or_create(session, self.models['location'],
                    site_id=r['siteID'],
                    domain=r['domainID'],
                    named_location=r['namedLocation'],
                    latitude=None,
                    longitude=None,
                    state=None,
                    country=None)

                spec = self.get_or_create(session, self.models['specimen'],
                    kingdom=r['kingdom'],
                    phylum=r['phylum'],
                    tax_class=r['class'],
                    order=r['order'],
                    family=r['family'],
                    subfamily=r['subfamily'],
                    tribe=r['tribe'],
                    genus=r['genus'],
                    subgenus=r['subgenus'],
                    species=r['specificEpithet'])

                samp = self.get_or_create(session, self.models['sample'],
                    set_date=r['setDate'],
                    collect_date=r['collectDate'],
                    location_id=loc[0].id)

                sci = self.get_or_create(session, self.models['scientist'],
                    name=self.handle_identified_by(r['identifiedBy']))

                lab = self.get_or_create(session, self.models['laboratory'],
                    name=r['laboratoryName'])

                subsamp = self.get_or_create(session, self.models['sub_sample'],
                    identified_by=sci[0].id,
                    identified_by_lab=lab[0].id,
                    individual_count=self.handle_individual_count(r['individualCount']),
                    sample_id=samp[0].id,
                    specimen_id=spec[0].id)
            except Exception as e:
                self.app.logger.error('Row: {} not inserted because of error {}'.format(r, e))

    def ingest_location_data(self):
        data = []
        session = self.db.session()
        with open(self.file_path) as f:
            reader = csv.DictReader(f)
            data = [r for r in reader]

        for r in data:
            try:
                nlcd = self.get_or_create(session, self.models['nlcd_class'],
                    name=r['nlcdClass'])

                point = 'SRID=4326;POINT({} {})'.format(r['decimalLatitude'], r['decimalLongitude'])
                session.query(self.models['location']).\
                    filter(self.models['location'].named_location == r['namedLocation']).\
                    update({
                        self.models['location'].elevation: self.handle_elevation(r['elevation']),
                        self.models['location'].nlcd_class_id: nlcd[0].id,
                        self.models['location'].point: point})

                session.commit()
            except Exception as e:
                self.app.logger.error('Row: {} not inserted because of error {}'.format(r, e))

    def get_or_create(self, session, model, **kwargs):
        instance = session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance, False
        else:
            params = dict((k, v) for k, v in kwargs.items())
            instance = model(**params)
            session.add(instance)
            session.commit()
            return instance, True

    def handle_individual_count(self, individual_count):
        try:
            if individual_count:
                return int(individual_count)
            else:
                return None
        except ValueError:
            return None

    def handle_elevation(self, elevation):
        try:
            if elevation:
                return float(elevation)
            else:
                return None
        except ValueError:
            return None

    # Names in the raw data are not always normalized
    # But this is terrible. There has to be another way.
    def handle_identified_by(self, identified_by):
        try:
            group_of_caps = re.findall('[A-Z][^A-Z]*', identified_by)
            # Handle Allysse's name
            if any('-' in g for g in group_of_caps):
                group_of_caps[-2] = group_of_caps[-2].strip() + group_of_caps[-1].strip()
                del group_of_caps[-1]
            i = 0
            while i < len(group_of_caps):
                group_of_caps[i] = group_of_caps[i].strip()
                i += 1
            last_name = group_of_caps.pop()
            first_initials = ''.join(group_of_caps)
            return first_initials + ' ' + last_name
        except Exception as e:
            self.app.logger.error('Error normalizing name {}: {}'.format(identified_by, e))
            return identified_by