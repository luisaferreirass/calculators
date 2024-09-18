from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError

class Calculator3:

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler        

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.calculate_multipliacation(input_data)
        self.__comparation(variance, multiplication)

        formated_response = self.__format_response(variance)
        return formated_response

    
    def __validate_body(self, body: List[float]) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_variance(self, input_data: List[float]) -> float:
        variance = self.__driver_handler.var(input_data)
        return variance
    
    def calculate_multipliacation(self, input_data: List[float]) -> float:
        multiplication = 1
        for num in input_data:
            multiplication *= num

        return multiplication

    
    def __comparation(self, variance: float, multiplication: float) -> None:

        if variance < multiplication:
            raise HttpBadRequestError('Falha no processo: Variância menor que multiplicação')
        

    def __format_response(self, variance: float) -> Dict:
        return {"data": {"calculator": 3,
                         "value": variance,
                         "Sucess": True}}






