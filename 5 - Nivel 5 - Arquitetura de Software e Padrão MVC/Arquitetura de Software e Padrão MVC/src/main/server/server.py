from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connect_handler

#Importar blueprints
from src.main.routes.pets_routes import pet_route_bp
from src.main.routes.person_routes import person_route_bp


db_connect_handler.conect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pet_route_bp)
app.register_blueprint(person_route_bp)


