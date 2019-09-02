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
    for filename in os.listdir('data/identification'):
        NeonIngestor(app, db, models, 'data/identification/' + filename).ingest_identification_data()

@manager.command
def ingestlocationdata():
    for filename in os.listdir('data/location'):
        NeonIngestor(app, db, models, 'data/location/' + filename).ingest_location_data()

if __name__ == '__main__':
    manager.run()