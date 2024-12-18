from flask import request as FlaskRequest
from typing import Dict
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator1:

    def calculate(self, request: FlaskRequest) -> Dict:
        data_input = request.json

        data_verify = self.__data_verify(data_input)

        number_splitted = data_verify / 3

        first_process_result = self.__first_process(number_splitted)
        second_process_result = self.__second_process(number_splitted)
        
        calc = first_process_result + second_process_result + number_splitted

        response = self.__format_response(calc)

        return response        


    def __data_verify(self, body: Dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")
        return body.get("number")

    def __first_process(self, number: float) -> float:

        first_part = (number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part 

    def __second_process(self, number:float) -> float:
        first_part = (number ** 2.121)
        second_part = (first_part / 5) + 1

        return second_part

    def __format_response(self, number: float) -> Dict:
        return {
            "data":{
                "Calculator": 1,
                "Result": round(number,2)
            }
        }