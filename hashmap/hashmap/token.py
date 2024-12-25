from enum import Enum, auto


class TokenType(Enum):
    
    NUMBER = auto()
    COMMA = auto()              # ,
    OPERATOR = auto()           # >= | <= | < | > | = | <>

    CHAR = auto()               # any other
    END = auto()                # 


class Token:

    def __init__(self, type_: TokenType, value: str) -> None:
        self.type_ = type_
        self.value = value

    def __str__(self) -> str:
        return f"({self.type_}: {self.value})"
