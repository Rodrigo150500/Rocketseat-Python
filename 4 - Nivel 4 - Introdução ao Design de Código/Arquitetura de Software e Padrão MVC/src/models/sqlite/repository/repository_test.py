import pytest
from ..settings.connection import db_connect_handler
from .pets_repository import PetsRepository

db_connect_handler.conect_to_db()

@pytest.mark.skip(reason="Interação com Banco de Dados")
def test_list_pets():
    repository = PetsRepository(db_connect_handler)

    response = repository.list_pets()

    print()
    print(response) 

def test_delete_pet():

    name = "belinha"
    
    repository = PetsRepository(db_connect_handler)

    repository.delete_pet(name)