from src.models.sqlite.settings.connection import db_connect_handler
from src.models.sqlite.repository.pets_repository import PetsRepository
from src.controller.pet_lister_controller import PetListerController
from src.views.pet_lister_view import PetListerView

def pet_lister_composer():

    model = PetsRepository(db_connect_handler)
    controller = PetListerController(model)
    view = PetListerView(controller)

    return view