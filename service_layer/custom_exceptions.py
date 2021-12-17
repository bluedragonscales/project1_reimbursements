

class InvalidAmountException(Exception):
    def __init__(self, message: str):
        self.message = message


class UnavailableException(Exception):
    def __init__(self, message: str):
        self.message = message


class WrongPasswordException(Exception):
    def __init__(self, message: str):
        self.message = message