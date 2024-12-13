from typing import Dict, List
from flask import request as FlaskRequest

class Calculator2():

    def calculate(self, request: FlaskRequest) -> Dict:
        
        data_input = request.json
        print(data_input)

        data_verify = self.__data_verify(data_input)
        print(data_verify)

    def __data_verify(self, body: Dict) -> List[float]:

        if "numbers" not in body:
            raise Exception("body mal formatado")
        
        input_data = body['numbers']
        return input_data
            