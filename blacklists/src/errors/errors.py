class ApiError(Exception):
    def __init__(self, description, code):
        self.description = description
        self.code = code


class InvalidToken(ApiError):
    def __init__(self):
        super().__init__("Unauthorized", 401)


class InvalidParams(ApiError):
    def __init__(self):
        super().__init__("Invalid parameters", 400)


class EmailAlreadyExists(ApiError):
    def __init__(self):
        super().__init__("Email already exists in the blacklist", 412)
