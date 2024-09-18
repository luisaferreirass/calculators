from .calculator_4 import Calculator4
from typing import Dict
from pytest import raises

class MockRequest():
    def __init__(self, body: Dict) -> None:
        self.json = body
        

def test_calculate():
    mock_request = MockRequest({
        "numbers": [1, 5, 7, 8, 45]
    })

    calculator = Calculator4()
    response = calculator.calculate(mock_request)

    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["Calculator"] == 4
    assert response["data"]["result"] == 13.2

def teste_calculate_with_error():
    mock_request = MockRequest({
        "num": [1, 5, 7, 8, 45]
    })

    calculator = Calculator4()
    
    with raises(Exception) as excinfo:
        calculator.calculate(mock_request)

    assert str(excinfo.value) == 'body mal formatado!'


