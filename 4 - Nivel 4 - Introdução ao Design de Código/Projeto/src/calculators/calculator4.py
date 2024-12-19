from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.drivers.interfaces.driver_handle_numpy import Driver_Handle_Numpy_Interface

class Calculator4:

    def __init__(self, handle_Driver: Driver_Handle_Numpy_Interface ) -> None:
        self.__handle_driver = handle_Driver

        
    def calculate(self, request: FlaskRequest) -> Dict:
        
        body = request.json

        data_input = self.__verify_data(body)

        media = self.__data_process(data_input)

        data_formated = self.__format_response(media)

        return data_formated
    
    def __verify_data(self, body: Dict) -> List[float]:

        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado!")
        
        response = body['numbers']
       
        return response
    
    def __data_process(self, numbers: List[float]) -> float:

        mean = self.__handle_driver.mean(numbers)
        
        return mean
        
        
    def __format_response(self, number: float) -> Dict:
        return {
            "data":{
                "Calculator": 4,
                "Result": round(number, 2)
            }
        }
