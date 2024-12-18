class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422

try:
    print("Estou no bloco try")
    raise HttpUnprocessableEntityError("Erro no processo")
except Exception as exception:
    print("Estou no bloco excelp")
    print(exception.message)
    print(exception.name)
    print(exception.status_code)
