from src.models.sqlite.settings.connection import db_connect_handler
from src.models.sqlite.repository.pets_repository import PetsRepository
from src.controller.pet_deleter_controller import PetDeleterController
from src.views.pet_deleter_view import PetDeleterView

def pet_deleter_composer():

    model = PetsRepository(db_connect_handler)
    controller = PetDeleterController(model)
    view = PetDeleterView(controller)

    return view