from .person_creator_validator import person_creator_validator
from src.views.http_types.http_request import HttpRequest

class MockRequest:

    def __init__(self, body: HttpRequest) -> None:
        self.body = body

def test_person_creator_validator():

    request = MockRequest({
        "first_name": "Rodrigo",
        "last_name": "Takara",
        "age": 24,
        "pet_id": 5
    })

    person_creator_validator(request)