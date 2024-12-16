from src.calculators.calculator2 import Calculator2
from src.drivers.numpy_handlers import Numpy_handlers

def calculator2_factory():

    numpy_driver_handler = Numpy_handlers()

    calc = Calculator2(numpy_driver_handler)

    return calc