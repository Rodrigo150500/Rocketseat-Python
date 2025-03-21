class HttpBadRequest(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.name = "HttpBadRequest"
        self.message = message
        self.status_code = 400