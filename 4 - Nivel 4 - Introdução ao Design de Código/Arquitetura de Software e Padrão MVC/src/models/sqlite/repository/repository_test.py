import pytest
from ..settings.connection import db_connect_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

db_connect_handler.conect_to_db()

@pytest.mark.skip(reason="Interação com Banco de Dados")
def test_list_pets():
    repository = PetsRepository(db_connect_handler)

    response = repository.list_pets()

    print()
    print(response) 

@pytest.mark.skip(reason="Interação com Banco de Dados")
def test_delete_pet():

    name = "belinha"
    
    repository = PetsRepository(db_connect_handler)

    repository.delete_pet(name)

@pytest.mark.skip(reason="Interação com Banco de Dados")
def test_insert_person():
    first_name = "First Name"
    last_name = "Last Name"
    age = 18
    pet_id = 2

    repo = PeopleRepository(db_connect_handler)

    repo.insert_person(first_name, last_name, age, pet_id)

def test_get_person():

    person_id = 1

    repo = PeopleRepository(db_connect_handler)

    response = repo.get_person(person_id)

    print()

    print(response)

    print(response.pet_name)
