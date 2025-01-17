from .pet_deleter_controller import PetDeleterController

def test_delete(mocker):

    mocker_repository = mocker.Mock()
    controller = PetDeleterController(mocker_repository)

    controller.delete("amiguinho")


    mocker_repository.delete_pet.assert_called_once_with("amiguinho") 