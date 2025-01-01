from ..settings.connection import db_connect_handler
from .pets_repository import PetsRepository

db_connect_handler.conect_to_db()

def test_list_pets():
    repository = PetsRepository(db_connect_handler)

    response = repository.list_pets()

    print()
    print(response)