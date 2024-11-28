from .token import Token, TokenType


class Lexer:
    def __init__(self) -> None:
        self._pos = 0
        self._text = ""
        self._current_char = None
        
    def init(self, s: str):
        self._pos = 0
        self._text = s
        self._current_char = self._text[0]
        
    def __forward(self):
        self._pos += 1
        if self._pos >= len(self._text):
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]
    
    def __skip(self):
        while (self._current_char is not None and self._current_char.isspace()):
            self.__forward()
    
    def __number(self):
        result = ""
        while (self._current_char is not None and
               (self._current_char.isdigit() or self._current_char == '.')):
            result += self._current_char
            if result.count('.') > 1:
                raise SyntaxError("Too many dots in number")
            self.__forward()
        return result    