from src.controllers.edit_balance_controller import EditBalanceController

class MockRepository:

    def edit_balance(self, userID, new_balance):
        pass


def test_edit_balance():

    mock_repository = MockRepository()

    controller = EditBalanceController(mock_repository)

    response = controller.edit("Rodrigo", 15)

    assert isinstance(response, dict)
    assert response['type'] == "User"
    assert response['count'] == 1
    assert response['new balance'] == 15
