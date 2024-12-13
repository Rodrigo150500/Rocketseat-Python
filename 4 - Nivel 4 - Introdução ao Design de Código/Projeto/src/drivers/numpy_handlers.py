import numpy
from typing import List

class Numpy_handlers():

    def __init__(self):
        self.__np = numpy

    
    def standart_deviation(self, numbers:List[float]) -> float:
        return self.__np.std(numbers)