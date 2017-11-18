# project/server

import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from project.server.auth.views import auth_blueprint
from project.server.getInfo.Question import question_blueprint
from project.server.getInfo.Zone import zone_blueprint
from project.server.getInfo.Branch import branch_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(question_blueprint)
app.register_blueprint(zone_blueprint)
app.register_blueprint(branch_blueprint)

