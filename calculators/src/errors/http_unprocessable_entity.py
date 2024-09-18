class HttpUnprocessableEntityError(Exception): #Estou falando que é uma classe de error
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422

