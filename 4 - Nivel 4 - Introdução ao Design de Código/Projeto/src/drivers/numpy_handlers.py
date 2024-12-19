import numpy
from typing import List
from .interfaces.driver_handle_numpy import Driver_Handle_Numpy_Interface

class Numpy_handlers(Driver_Handle_Numpy_Interface):

    def __init__(self):
        self.__np = numpy

    
    def standart_deviation(self, numbers:List[float]) -> float:
        return self.__np.std(numbers)

    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)

    def mean(self, numbers: List[float]) -> float:
        return self.__np.mean(numbers)