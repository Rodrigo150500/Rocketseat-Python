from .calculator3 import Calculator3
from typing import List
from pytest import raises

class MockRequest:
    def __init__(self, body) -> None:
        self.json = body

class MockDriverHandleError:
    def variance(self, numbers: List[float]) -> float:
        return 3

class MockDriverHandle:
    def variance(self, numbers: List[float]) -> float:
        return 1000000

def test_calculate_with_body_error():

    mockRequest = MockRequest({'numbers': [1,2,3,4,5]})

    calculator = Calculator3(MockDriverHandleError())

    with raises(Exception) as exceptInfo:
        calculator.calculate(mockRequest)

    assert str(exceptInfo.value) == 'Variação menor do que a multiplicao!'

def test_calculate():

    mockRequest = MockRequest({'numbers': [1,1,1,1,100]})

    calculator = Calculator3(MockDriverHandle())

    response = calculator.calculate(mockRequest)

    assert response == {'data': {'Calculator': 3, 'Result': 1000000, 'Validation': True}}


