from .calculator2 import Calculator2
from pytest import raises

class MockRequest():
    def __init__(self, body):
        self.json = body

def test_calc2():

    request = MockRequest({'numbers' : [1.53, 2.59, 8.66, 3.63]})


    calculator_2 = Calculator2()
    format_response = calculator_2.calculate(request)

    assert isinstance(format_response, dict) #Verificando se o format_response é um dicionário 
    assert format_response =={'data': {'Calculator': 2, 'Result': 0.04}}

def test_body_bad_formated():

    request = MockRequest({"algo":[3, 5.9, 33]})

    calc = Calculator2()

    with raises(Exception) as exception:
        calc.calculate(request)

    assert str(exception.value) == "body mal formatado"
