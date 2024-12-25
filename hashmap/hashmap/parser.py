from .ast import Condition, Value
from .lexer import Lexer
from .token import TokenType, Token
from .exceptions import InvalidTokenOrder


class Parser:
    
    def __init__(self) -> None:
        self._current_token = None
        self._lexer = Lexer()

    def __check_token(self, type_: TokenType) -> None:
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise InvalidTokenOrder(str(type_), str(self._current_token.type_))

    def __operator(self) -> Token:
        token = self._current_token
        self.__check_token(TokenType.OPERATOR)
        return token
    
    def __number(self) -> Token:
        token = self._current_token
        self.__check_token(TokenType.NUMBER)
        return token

    def __condition(self) -> Condition:
        operator = self.__operator()
        value = self.__number()
        return Condition(operator, value)

    def __list(self, waiting: str = 'condition') -> list:
        waitings = ('condition', 'number')
        if waiting not in waitings:
            raise AttributeError(f"Waiting attribute must be in {waitings}")

        array = list()
        waiting_end = False
        while True:
            token = self._current_token
            if waiting_end and token.type_ == TokenType.END:
                return array
            elif token.type_ == TokenType.CHAR or token.type_ == TokenType.END:
                return list()
            else:
                if waiting == 'condition':
                    item = self.__condition()
                else:
                    item = Value(self.__number())
                array += [item]
                if self._current_token.type_ == TokenType.COMMA:
                    self.__check_token(TokenType.COMMA)
                else:
                    waiting_end = True
    
    def get_conditions(self, s: str) -> list:
        self._lexer.init(s)
        self._current_token = self._lexer.next()

        return self.__list(waiting='condition')
    
    def get_values(self, s: str) -> list:
        self._lexer.init(s)
        self._current_token = self._lexer.next()

        return self.__list(waiting='number')
