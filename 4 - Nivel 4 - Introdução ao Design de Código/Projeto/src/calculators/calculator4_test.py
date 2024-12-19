from calculators.calculator4 import Calculator4
from drivers.numpy_handlers import Numpy_handlers
from typing import Dict
from pytest import raises

class MockRequest:

    def __init__(self, body) -> None:
        self.json = body


def test_calc():

    request = MockRequest({'numbers': [1,2,3,4,5]})
    
    calc = Calculator4(Numpy_handlers())
    
    reponse = calc.calculate(request)

    assert reponse == {'data': {'Calculator': 4, 'Result': 3.0}}
    assert isinstance(reponse, Dict)

def test_calc_with_formatation():

    request = MockRequest({'numers': [1,3,5.9,6]})

    calc = Calculator4(Numpy_handlers())

    with raises(Exception) as exception:
        calc.calculate(request)

    assert str(exception.value) == "Body mal formatado!"