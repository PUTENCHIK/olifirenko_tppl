from .token import Token, TokenType


class Lexer():
    
    def __init__(self) -> None:
        self._pos = 0
        self._text = ""
        self._current_char = None
        
    def init(self, s: str):
        self._text = s
        self._pos = 0
        self._current_char = self._text[self._pos]
        
    def __forward(self):
        self._pos += 1
        if self._pos > len(self._text)-1:
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]
        
    def __skip(self):
        while (self._current_char is not None and 
               self._current_char.isspace()):
            self.__forward()
            
    def __integer(self):
        result = ""
        while (self._current_char is not None and
               self._current_char.isdigit()):
            result += self._current_char
            self.__forward()
        return result       
            
    def __number(self):
        result = ""
        while (self._current_char is not None and
               (self._current_char.isdigit() or self._current_char == '.')):
            result += self._current_char
            if result.count('.') > 1:
                raise SyntaxError("Too many dots in number")
            self.__forward()
        return result        
    
    def next(self) -> Token:
        while self._current_char:
            if self._current_char.isspace():
                self.__skip()
                continue
            elif self._current_char.isdigit():
                return Token(TokenType.NUMBER, self.__number())
            elif self._current_char in ('-', '+', '*', '/'):
                op = self._current_char
                self.__forward()
                return Token(TokenType.OPERATOR, op)
            elif self._current_char == '(':
                val = self._current_char
                self.__forward()
                return Token(TokenType.LPAREN, val)
            elif self._current_char == ')':
                val = self._current_char
                self.__forward()
                return Token(TokenType.RPAREN, val)
            else:
                raise SyntaxError(f"Bad token: {self._current_char}")
        return Token(TokenType.EOL, "")
    
    
    
    
