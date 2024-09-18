from typing import List, Dict
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator2:


    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__diver_handler = driver_handler
        

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        first_list = self.__validate_body(body)
        final_result = self.__process(first_list)

        response = self.__format_response(final_result)
        return response


    def __validate_body(self, body: List[float]) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")
        
        input_data = body["numbers"]
        return input_data

    def __process(self, first_list: List[float]) -> float:
        second_list = [(num * 11) ** 0.95 for num in first_list]
        result = self.__diver_handler.standard_derivation(second_list)
        return 1/result
    
    def __format_response(self, final_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(final_result, 2)
            }
        }


        


        
        


          
