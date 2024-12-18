from src.calculators.calculator3 import Calculator3
from src.drivers.numpy_handlers import Numpy_handlers

def calculator3_factory():

    numpy_handler = Numpy_handlers()

    calc = Calculator3(numpy_handler)
    
    return calc