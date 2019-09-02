import os
from flask_script import Shell, Manager, prompt, prompt_bool
from flask_migrate import Migrate, MigrateCommand

from app import app, db, models
from ingestors.neon_ingestor import NeonIngestor

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

def _make_context():
    return dict(
        app=app,
        db=db,
        NeonIngestor=NeonIngestor,
        models=models
    )

manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=_make_context))

@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to lose all your data"):
        db.drop_all()

@manager.command
def ingestiddata():
    i = 0
    for filename in os.listdir('data/identification'):
        NeonIngestor(app, db, models, 'data/identification/' + filename).ingest_identification_data()
        i += 1
        printProgressBar(i, len(os.listdir('data/identification')))

@manager.command
def ingestlocationdata():
    i = 0
    for filename in os.listdir('data/location'):
        NeonIngestor(app, db, models, 'data/location/' + filename).ingest_location_data()
        i += 1
        printProgressBar(i, len(os.listdir('data/location')))

def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
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
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

if __name__ == '__main__':
    manager.run()