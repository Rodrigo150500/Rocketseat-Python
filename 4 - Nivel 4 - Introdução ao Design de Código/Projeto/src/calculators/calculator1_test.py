from calculators.calculator1 import Calculator1
from typing import Dict
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict):
        self.json = body

def test_calc():
    request = MockRequest(body={"number": 5})

    calc = Calculator1()
    response = calc.calculate(request)

    #Testando formatação
    assert "data" in response
    assert "Calculator" in response['data']
    assert "Result" in response['data']

    #Testando resultado
    assert response['data']['Calculator'] == 1
    assert response['data']['Result'] == 17.39

def test_calculate_with_bodu_error():

    request = MockRequest(body= {"something": 5})

    calc = Calculator1()

    with raises(Exception) as exception:
        calc.calculate(request)
    
    assert str(exception.value) == "body mal formatado!"
    
