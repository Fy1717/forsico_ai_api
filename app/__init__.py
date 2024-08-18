import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv


def createApp():
    load_dotenv('forsico.env')  # Ensure the .env file is loaded

    app = Flask(__name__, static_url_path="")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DB_URI", "postgresql://postgres:postgres@localhost:5432/"
        + "forsico_io_ai")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["UPLOAD_FOLDER"] = os.getenv("UPLOAD_FOLDER")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SUPER_ADMIN_SECRET_KEY"] = os.getenv("SUPER_ADMIN_SECRET_KEY")
    app.config["INSTITUTION_ADMIN_SECRET_KEY"] = os.getenv(
        "INSTITUTION_ADMIN_SECRET_KEY")
    app.config["ATTENDANT_SECRET_KEY"] = os.getenv("ATTENDANT_SECRET_KEY")
    CORS(app)
    db = SQLAlchemy(app)
    Migrate(app, db)

    return app
