class HttpRequest:
    
    def __init__(self, 
        body: dict = None,
        params:dict = None,
        header: dict = None,
        token_info: dict = None):

        self.body = body
        self.params = params
        self.header = header
        self.token_info = token_info
    