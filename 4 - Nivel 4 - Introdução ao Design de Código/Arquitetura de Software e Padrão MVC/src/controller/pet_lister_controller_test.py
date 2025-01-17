from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsController:
    def list_pets(self):
        return [
            PetsTable(name='Fluffy', type="dog", id = 3),
            PetsTable(name="Buddy", type="cat", id=42)
        ]

def test_list_pet():
    controller = PetListerController(MockPetsController())

    response = controller.list()

    expected_response = {
        "data":{
                "type": "Pets",
                "count":2,
                "attributes": [
                    {"pet_name": "Fluffy","id": 3},
                    {"pet_name": "Buddy","id": 42}
                    ]
            }
    }

    assert response == expected_response