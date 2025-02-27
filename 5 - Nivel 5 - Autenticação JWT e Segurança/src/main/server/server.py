from flask import Flask
from src.models.settings.db_connecting_handler import db_connection_handler
from src.main.routes.bank_account_routes import bank_account_bp

db_connection_handler.connect()

app = Flask(__name__)

app.register_blueprint(bank_account_bp)