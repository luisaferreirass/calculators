from typing import Dict
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator1:

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        data = request.json
        input_data = self.__validate_body(data)
        splited_number = input_data / 3
        
        first_result = self.__first_process(splited_number)
        second_result = self.__second_process(splited_number)
        third_result = self.__third_process(splited_number)
        final_result = first_result + second_result + third_result

        response = self.__format_response(final_result)
        return response


    def __validate_body(self, data: Dict) -> float:
        if "number" not in data:
            raise HttpUnprocessableEntityError("body mal formatado")
        
        input_data = data["number"]
        return input_data
    
    def __first_process(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part
    
    def __second_process(self, second_number: float) -> float:
        first_part = (second_number ** 2.121) / 5
        second_part = first_part + 1
        return second_part
    
    def __third_process(self, third_number: float) -> float:
        return third_number

    def __format_response(self, final_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 1,
                "result": round(final_result, 2)
            }
        }

