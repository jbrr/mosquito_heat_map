from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import jsonify
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

from models.location import Location
from models.sample import Sample
from models.sub_sample import SubSample
from models.specimen import Specimen
from models.scientist import Scientist
from models.laboratory import Laboratory
from models.nlcd_class import NlcdClass
from utils import Utils

models = {
    'location': Location,
    'sample': Sample,
    'sub_sample': SubSample,
    'specimen': Specimen,
    'scientist': Scientist,
    'laboratory': Laboratory,
    'nlcd_class': NlcdClass
}

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/api/v0/locations')
def get_locations():
    locs = db.session.query(models['location']).all()
    geojson = Utils.to_geojson(locs)
    return jsonify(geojson)

if __name__ == '__main__':
    app.run()