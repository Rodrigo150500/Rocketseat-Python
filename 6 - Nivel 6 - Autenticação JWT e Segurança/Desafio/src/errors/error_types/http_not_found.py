class HttpNotFound(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.name = "HttpNotFound"
        self.message = message
        self.status_code = 404