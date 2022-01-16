

class InvalidAmountException(Exception):
    def __init__(self, message: str):
        self.message = message


class UnavailableException(Exception):
    def __init__(self, message: str):
        self.message = message


class CredentialsFalseException(Exception):
    def __init__(self, message: str):
        self.message = message


class SpacesException(Exception):
    def __init__(self, message: str):
        self.message = message


class NonExistentEmployeeException(Exception):
    def __init__(self, message: str):
        self.message = message