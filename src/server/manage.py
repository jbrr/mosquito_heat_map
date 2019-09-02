import os
from flask_script import Shell, Manager, prompt, prompt_bool
from flask_migrate import Migrate, MigrateCommand

# from app import app, db, CsvImporter, location, sample, sub_sample, specimen
import app
from ingestors.neon_ingestor import NeonIngestor

app.app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app.app, app.db)
manager = Manager(app.app)

def _make_context():
    return dict(
        app=app.app,
        db=app.db,
        NeonIngestor=NeonIngestor,
        models=app.models
    )

manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=_make_context))

@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to lose all your data"):
        app.db.drop_all()

@manager.command
def importcsvs():
    for filename in os.listdir('data/unprocessed'):
        NeonIngestor(app.app, app.db, app.models, 'data/unprocessed/' + filename).import_csv()

if __name__ == '__main__':
    manager.run()