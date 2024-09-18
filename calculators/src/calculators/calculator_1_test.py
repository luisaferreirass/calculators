from .calculator_1 import Calculator1
from typing import Dict
from pytest import raises

class MockRequest: # Classe para simularmos uma requisição real no teste já que o teste tem um request
    def __init__(self, body: Dict) -> None:
        self.json = body # Estamos basicamente tranformando o body em json

def test_calculate():
    mock_request = MockRequest(body={
        "number": 1
    })
    calculator_1 =  Calculator1()

    response = calculator_1.calculate(mock_request)

    # Formato da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # Assertividade da resposta
    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1

def test_calculate_with_body_error():
    mock_request = MockRequest(body={
        "something": 1
    })

    calculator_1 =  Calculator1()

    # Se for lançada qualquer exceção nessa execução vai ser colocada no excinfo
    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request)

    assert str(excinfo.value) == 'body mal formatado'

    




