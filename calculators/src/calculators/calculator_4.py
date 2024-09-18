from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
    
class Calculator4:
    def calculate(self, request: FlaskRequest) -> float: # type: ignore
        body = request.json
        input_data = self.__validade_body(body)
        result = self.__media(input_data)
        response = self.__format_response(result)

        return response

    def __validade_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")
        
        input_data = body['numbers']
        return input_data
    
    def __media(self, input_data: List[float]) -> float:
        sum = 0
        for num in input_data:
            sum += num

        media = sum / len(input_data)

        return media
    
    def __format_response(self, result: float) -> Dict:
        return {"data": {
            "Calculator": 4,
            "result": result
        }}

    

