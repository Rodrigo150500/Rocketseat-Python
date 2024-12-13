from typing import Dict, List
from flask import request as FlaskRequest
from drivers.numpy_handlers import Numpy_handlers

class Calculator2():

    def calculate(self, request: FlaskRequest) -> Dict:
        
        data_input = request.json

        data_verify = self.__data_verify(data_input)

        data_process_result = self.__data_process(data_verify)
        print()
        print(data_process_result)
        result = self.__format_response(data_process_result)

        print(result)

        return result

    def __data_verify(self, body: Dict) -> List[float]:

        if "numbers" not in body:
            raise Exception("body mal formatado")
        
        input_data = body['numbers']
        
        return input_data
    
    def __data_process(self, data_input: List[float]) -> float:
        first_process = [(num * 11) ** 0.95 for num in data_input]

        numpy_handler = Numpy_handlers()
        standart_deviation = numpy_handler.standart_deviation(first_process)
        
        return 1/standart_deviation

    def __format_response(self, result: float) -> Dict:
        return {
            "data":{
                "Calculator": 2,
                "Result": round(float(result), 2)
            }
        }