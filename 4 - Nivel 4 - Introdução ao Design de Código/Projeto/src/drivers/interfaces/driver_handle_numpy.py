from abc import ABC, abstractmethod
from typing import List

class Driver_Handle_Numpy(ABC):

    @abstractmethod
    def standart_deviation(self, numbers:List[float]) -> float:
        pass
