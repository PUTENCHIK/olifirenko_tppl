from .token import Token, TokenType
from .exceptions import TooManyDotsInNumber, BadOperatorToken


class Lexer:

    skipable = ('(', ')')
    operators = ('>', '<', '=')
    
    def __init__(self) -> None:
        self._pos = None
        self._text = None
        self._current_char = None

    def init(self, s: str) -> None:
        self._pos = -1
        self._text = s
        self.__forward()

    def __forward(self):
        self._pos += 1
        if self._pos >= len(self._text):
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]
    
    def __skip(self):
        while (self._current_char is not None and
               (self._current_char.isspace() or self._current_char in Lexer.skipable)):
            self.__forward()

    def __number(self) -> str:
        result = ""
        while (self._current_char is not None and
               (self._current_char.isdigit() or self._current_char == '.')):
            result += self._current_char
            if result.count('.') > 1:
                raise TooManyDotsInNumber
            self.__forward()
        return result
    
    def __operator(self) -> str:
        result = ""
        while (self._current_char is not None and
               self._current_char in Lexer.operators):
            result += self._current_char
            if result not in ('=', '>', '<', '<>', '>=', '<='):
                raise BadOperatorToken
            self.__forward()
        return result

    def next(self) -> Token:
        while self._current_char:
            if self._current_char.isspace() or self._current_char in Lexer.skipable:
                self.__skip()
                continue
            elif self._current_char.isdigit():
                return Token(TokenType.NUMBER, self.__number())
            elif self._current_char == ',':
                comma = self._current_char
                self.__forward()
                return Token(TokenType.COMMA, comma)
            elif self._current_char in Lexer.operators:
                return Token(TokenType.OPERATOR, self.__operator())
            else:
                char = self._current_char
                self.__forward()
                return Token(TokenType.CHAR, char)

        return Token(TokenType.END, "")
