

class InvalidAmountException(Exception):
    def __init__(self, message: str):
        self.message = message


class ListUnavailableException(Exception):
    def __init__(self, message: str):
        self.message = message