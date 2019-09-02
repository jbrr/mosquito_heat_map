from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models.location import Location
from models.sample import Sample
from models.sub_sample import SubSample
from models.specimen import Specimen
from models.scientist import Scientist
from models.laboratory import Laboratory
from models.nlcd_class import NlcdClass

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

if __name__ == '__main__':
    app.run()