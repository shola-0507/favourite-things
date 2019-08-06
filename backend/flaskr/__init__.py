import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS
from flaskr.system.config import config

project_dir = os.path.dirname(os.path.abspath(__file__))
database_conn = "mysql+pymysql://" + config["database"]["sql"]["user"] + ":" + config["database"]["sql"]["pass"] \
                    + "@" + config["database"]["sql"]["host"] + ":" + str(config["database"]["sql"]["port"]) + "/" + \
                    config["database"]["sql"]["name"]


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    CORS(app, supports_credentials=True)

    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        # load the models config, if it exists, when not testing
        app.config['SQLALCHEMY_DATABASE_URI'] = database_conn
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return jsonify({"data": "Hello World"})

    return app


app = create_app()
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

from . import category
app.register_blueprint(category.bp)

from . import item
app.register_blueprint(item.bp)

from .import auditLog
app.register_blueprint(auditLog.bp)
