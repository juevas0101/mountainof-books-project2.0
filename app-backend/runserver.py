import os
from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from .src.routes.blueprint.blueprint_model import all_blueprint
from .src.models import db

def create_app(testing_config=None):
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, './src/data/database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if testing_config:
        app.config.update(testing_config)

    load_dotenv(".env")

    db.init_app(app)

    __ = Migrate(app, db, directory="./src/data")

    for _, blueprint in all_blueprint.items():
        app.register_blueprint(blueprint)

    return app

if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True)
