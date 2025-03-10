from .user_repository import UserRepository
from src.models.settings.conection import db_conection_handler




def test_registry_user_integration():

    db_conection_handler.connect()

    conn = db_conection_handler.get_connection()

    repo = UserRepository(conn)

    username = "Rodrigo"
    password = "ABC123"

    repo.registry_user(username, password)