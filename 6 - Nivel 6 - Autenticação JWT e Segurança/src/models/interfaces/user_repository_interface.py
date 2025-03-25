from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):

    @abstractmethod
    def registry_user(self, username: str, password: str) -> None: pass

    @abstractmethod
    def edit_balance(self, userID: int, balance: float) -> None: pass
    
    @abstractmethod
    def get_user_by_username(self, username: str) -> tuple[int, str, str]: pass