from .calculator2 import Calculator2
from pytest import raises
from drivers.numpy_handlers import Numpy_handlers
from typing import List, Dict

class MockRequest():
    def __init__(self, body: Dict):
        self.json = body

class MockDriver():
    def standart_deviation(self, numbers:List[float]) -> float:
        return 3

def test_calc2_integration():

    request = MockRequest({'numbers' : [1.53, 2.59, 8.66, 3.63]})
    
    drive = Numpy_handlers()

    calculator_2 = Calculator2(drive)
    format_response = calculator_2.calculate(request)

    assert isinstance(format_response, dict) #Verificando se o format_response é um dicionário 
    assert format_response =={'data': {'Calculator': 2, 'Result': 0.04}}

def test_calc2():

    request = MockRequest({'numbers' : [1.53, 2.59, 8.66, 3.63]})
    
    drive = MockDriver()

    calculator_2 = Calculator2(drive)
    format_response = calculator_2.calculate(request)

    assert isinstance(format_response, dict) #Verificando se o format_response é um dicionário 
    assert format_response =={'data': {'Calculator': 2, 'Result': 0.33}}


def test_body_bad_formated():

    request = MockRequest({"algo":[3, 5.9, 33]})

    drive = Numpy_handlers()

    calc = Calculator2(drive)

    with raises(Exception) as exception:
        calc.calculate(request)

    assert str(exception.value) == "body mal formatado"

