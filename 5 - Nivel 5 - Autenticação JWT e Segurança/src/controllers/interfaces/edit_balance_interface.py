from abc import ABC, abstractmethod

class EditBalanceInterface(ABC):
    def edit(self, user_id: int, new_balance: float) -> dict:
        pass