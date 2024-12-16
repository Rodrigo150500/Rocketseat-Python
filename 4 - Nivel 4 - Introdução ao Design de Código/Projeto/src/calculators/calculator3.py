from drivers.interfaces.driver_handle_numpy import Driver_Handle_Numpy_Interface
from flask import request as FlaskRequest
from typing import Dict, List

class Calculator3:

    def __init__(self, driver_handler: Driver_Handle_Numpy_Interface) -> None:
        self.__driver_handler = driver_handler
    
    def calculate(self, request: FlaskRequest) -> Dict:
        
        data_verify = self.__verify_data(request.json)

        variance = self.__variance(data_verify)
        multiplication = self.__multiplication(data_verify)

        self.__response_validation(variance, multiplication)

        response = self.__format_response(variance)

        return response

    def __verify_data(self, body: Dict) -> List[float]:

        if 'numbers' not in body:
            raise Exception("Body mal formatado!")

        response = body['numbers']

        return response
        

    def __variance(self, numbers: List[float]) -> float:
        return self.__driver_handler.variance(numbers)

    def __multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers: multiplication *= num

        return multiplication

    def __response_validation(self, variance: float, multiplication: float) -> None:

        if variance < multiplication:
            raise Exception('Variação menor do que a multiplicao!')

    def __format_response(self, variance):
        return {
            'data':{
                "Calculator": 3,
                "Result": round(variance, 2),
                "Validation": True
            }
        }