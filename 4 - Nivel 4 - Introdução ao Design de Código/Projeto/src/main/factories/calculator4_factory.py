from src.calculators.calculator4 import Calculator4
from src.drivers.numpy_handlers import Numpy_handlers

def calculator4_factory():

    calc = Calculator4(Numpy_handlers())

    return calc