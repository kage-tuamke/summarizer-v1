from app.modules.transcripts.route import transcripts_bp
from app.modules.auth.route import auth_bp
from app.modules.processor.route import processor_bp
from flask import Flask
from flasgger import Swagger
from app.db.db import db


def initialize_route(app: Flask):
    with app.app_context(): 
        app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
        app.register_blueprint(transcripts_bp, url_prefix='/api/v1/transcripts')
        app.register_blueprint(processor_bp, url_prefix='/api/v1/processor')        

def initialize_db(app: Flask):
    with app.app_context():
        db.init_app(app)
        db.create_all()

def initialize_swagger(app: Flask):
    with app.app_context():
        swagger = Swagger(app)
        return swagger
