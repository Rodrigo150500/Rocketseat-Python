from src.models.interfaces.user_repository_interface import UserRepositoryInterface

class UserRegistry:
    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.__repository = repository