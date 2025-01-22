from src.models.sqlite.settings.connection import db_connect_handler
from src.models.sqlite.repository.people_repository import PeopleRepository
from src.controller.person_finder_controller import PersonFinderController
from src.views.person_finder_view import PersonFinderView

def person_finder_composer():

    model = PeopleRepository(db_connect_handler)
    controller = PersonFinderController(model)
    view = PersonFinderView(controller)

    return view