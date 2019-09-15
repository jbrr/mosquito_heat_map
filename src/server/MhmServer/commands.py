import os
import click
from flask.cli import with_appcontext
from MhmServer.ingestors.neon_ingestor import NeonIngestor
from MhmServer.database import db
import MhmServer.models as models


models = dict(laboratory=models.Laboratory, location=models.Location,
              nlcd_class=models.NlcdClass, sample=models.Sample, scientist=models.Scientist,
              specimen=models.Specimen, sub_sample=models.SubSample)


@click.command()
@with_appcontext
def ingestiddata():
    i = 0
    for filename in os.listdir('data/identification'):
        NeonIngestor(db, models, 'data/identification/' + filename).ingest_identification_data()
        i += 1
        print_progress_bar(i, len(os.listdir('data/identification')))


@click.command()
@with_appcontext
def ingestlocationdata():
    i = 0
    for filename in os.listdir('data/location'):
        NeonIngestor(db, models, 'data/location/' + filename).ingest_location_data()
        i += 1
        print_progress_bar(i, len(os.listdir('data/location')))


def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()
