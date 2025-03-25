from flask import Flask
from src.main.routes.tasks_route import tasks_routes_bp
from src.models.settings.conection import db_conection_handler

db_conection_handler.connect()

app = Flask(__name__)

app.register_blueprint(tasks_routes_bp)