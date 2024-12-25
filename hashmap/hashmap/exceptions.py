class TooManyDotsInNumber(Exception):
    pass

class BadOperatorToken(Exception):
    pass

class InvalidTokenOrder(SyntaxError):
    def __init__(self, expected: str, gotten: str):
        super().__init__(f"expected {expected}, gotten {gotten}")
