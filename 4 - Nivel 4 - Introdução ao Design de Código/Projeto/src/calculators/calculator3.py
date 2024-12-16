from src.drivers.interfaces.driver_handle_numpy import Driver_Handle_Numpy_Interface
from flask import request as FlaskRequest
from typing import Dict

class Calculator3:

    def __init__(self, driver_handler: Driver_Handle_Numpy_Interface) -> None:
        self.__driver_handler = driver_handler
    
    def calculate(self, request: FlaskRequest) -> Dict:
        pass