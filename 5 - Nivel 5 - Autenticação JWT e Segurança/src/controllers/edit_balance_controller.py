from src.models.interfaces.user_repository_interface import UserRepositoryInterface
from .interfaces.edit_balance_interface import EditBalanceInterface

class EditBalanceController(EditBalanceInterface):

    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.__repository = repository

    def edit(self, user_id: int, new_balance: float) -> dict:
        self.__repository.edit_balance(user_id, new_balance)

        return {
            "type": "User",
            "count": 1,
            "new balance": new_balance
        }
