from src.models.sqlite.repository.people_repository import PeopleRepository
from src.models.sqlite.settings.connection import db_connect_handler
from src.views.person_creator_view import PersonCreatorView
from src.controller.person_creator_controller import PersonCreatorController

def person_creator_composer():

    model = PeopleRepository(db_connect_handler)
    controller = PersonCreatorController(model)
    view = PersonCreatorView(controller)

    return view