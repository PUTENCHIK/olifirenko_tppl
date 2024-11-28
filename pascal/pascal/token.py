from enum import Enum, auto


class TokenType(Enum):
    DOT = auto()
    BEGIN = auto()
    END = auto()
    
    NUMBER = auto()
    OPERATOR = auto() 
       
    LPAREN = auto()
    RPAREN = auto()
    ASSIGN = auto
    SEMICOLON = auto()
    
    EOL = auto()
    
    
class Token:
    def __init__(self, type_: TokenType, value: str) -> None:
        self.type_ = type_
        self.value = value
        
    def __str__(self) -> str:
        return f"({self.type_}: {self.value})"
