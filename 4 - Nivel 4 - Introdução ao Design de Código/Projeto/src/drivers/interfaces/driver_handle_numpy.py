from abc import ABC, abstractmethod
from typing import List

class Driver_Handle_Numpy_Interface(ABC):

    @abstractmethod
    def standart_deviation(self, numbers:List[float]) -> float:
        pass

    @abstractmethod    
    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)