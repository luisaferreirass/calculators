




class HttpUnprocessableEntityError(Exception): #Estou falando que é uma classe de error
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422

try:
    print('Esrou no bloco try')
    raise HttpUnprocessableEntityError('Estou lançando a exception')
except Exception as exception:
    print(exception.name)
    print(exception.status_code)