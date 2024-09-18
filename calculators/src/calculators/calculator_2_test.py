from .calculator_2 import Calculator2
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest: # Classe para simularmos uma requisição real no teste já que o teste tem um request
    def __init__(self, body: Dict) -> None:
        self.json = body # Estamos basicamente tranformando o body em json

class MockDriverHandler:
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3 # Vamos utilizar um elemento ficticio e controlado para testar a lógica da calculadora 2


# Está testando a integração entre NumpyHandler e Calculator2
def test_calculate_integration():
    mock_request = MockRequest(body={
        "numbers": [1.5, 2.4, 3.79, 4, 5]
    })

    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)

    # Formato da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    assert isinstance(response, dict) #Para confirmar se o tipo é igual a um dicionário

def test_calculate():
    mock_request = MockRequest(body={
        "numbers": [1.5, 2.4, 3.79, 4, 5]
    })

    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)

    # Formato da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    assert isinstance(response, dict) #Para confirmar se o tipo é igual a um dicionário
    assert response == {'data': {'Calculator': 2, 'result': 0.33}}

    
    