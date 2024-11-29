class TooManyDotsInNumber(Exception):
    pass


class BadToken(Exception):
    def __init__(self, token: str):
        super().__init__(f"'{token}'")


class InvalidTokenOrder(SyntaxError):
    def __init__(self, expected: str, gotten: str):
        super().__init__(f"expected {expected}, gotten {gotten}")


class InvalidFactor(SyntaxError):
    def __init__(self, token: str):
        super().__init__(token)


class InvalidSyntaxOfStatement(SyntaxError):
    pass


class ExtraSemicolon(SyntaxError):
    def __init__(self):
        super().__init__("extra ; in end of statement list")


class UnkownVariable(Exception):
    def __init__(self, name: str):
        super().__init__(f"'{name}' is not defined")
