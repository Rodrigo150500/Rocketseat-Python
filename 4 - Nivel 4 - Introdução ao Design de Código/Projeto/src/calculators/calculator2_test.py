from .calculator2 import Calculator2

class MockRequest():
    def __init__(self, body):
        self.json = body

def test_calc2():

    request = MockRequest({'numbers' : [1.53, 2.59, 8.66, 3]})


    calculator_2 = Calculator2()
    data_input = calculator_2.calculate(request)
