from abc import ABC, abstractmethod
from typing import List
from ..entities.pets import PetsTable


class PetsRepositoryInterface:

    @abstractmethod
    def list_pets(self) -> List[PetsTable]:
        pass

    @abstractmethod
    def delete_pet(self, name: str) -> None:
        pass


