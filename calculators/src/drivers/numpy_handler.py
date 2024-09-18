# Gerente a biblioteca externa (numpy)
import numpy
from typing import List
from .interfaces.driver_handler_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers) # Estamos padronizando
    
    def var(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)

# Essa classe vai ter um atributo que é direcionado ao numpy