from enum import Enum, auto


class TokenType(Enum):
    BEGIN = auto()              # BEGIN
    END = auto()                # END

    NUMBER = auto()             # int | float
    VARIABLE = auto()           # variable
    OPERATOR = auto()           # + | - | / | *
       
    LPAREN = auto()             # (
    RPAREN = auto()             # )
    EQUAL = auto()              # =
    COLON = auto()              # :
    SEMICOLON = auto()          # ;
    DOT = auto()                # .
    
    EOL = auto()                # \0
    
    
class Token:
    def __init__(self, type_: TokenType, value: str) -> None:
        self.type_ = type_
        self.value = value
        
    def __str__(self) -> str:
        return f"({self.type_}: {self.value})"
