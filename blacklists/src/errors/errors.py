class ApiError(Exception):
    def __init__(self, description, code):
        self.description = description
        self.code = code


class InvalidParams(ApiError):
    def __init__(self):
        super().__init("Invalid parameters", 400)


class EmailAlreadyExists(ApiError):
    def __init__(self):
        super().__init("Email already exists in the blacklist", 409)
