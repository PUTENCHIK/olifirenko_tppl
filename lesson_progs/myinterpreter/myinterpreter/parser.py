from .token import TokenType
from .lexer import Lexer
from .ast import BinOp, Number, UnaryOp


class Parser():
    
    def __init__(self) -> None:
        self._current_token = None
        self._lexer = Lexer()
    
    def __check_token(self, type_: TokenType) -> None:
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise SyntaxError(f"Invalid token order: {type_}")  
        
    def __factor(self):
        token = self._current_token
        
        if token.value == "+":
            self.__check_token(TokenType.OPERATOR)
            return UnaryOp(token, self.__factor())
        elif token.value == "-":
            self.__check_token(TokenType.OPERATOR)
            return UnaryOp(token, self.__factor())
            
        if token.type_ == TokenType.NUMBER:
            self.__check_token(TokenType.NUMBER)
            return Number(token)
        elif token.type_ == TokenType.LPAREN:
            self.__check_token(TokenType.LPAREN)
            result = self.__expr()
            self.__check_token(TokenType.RPAREN)
            return result
        else:
            raise SyntaxError("Invalid factor")
        
    def __term(self) -> BinOp:
        result = self.__factor()
        while self._current_token and (self._current_token.type_ == TokenType.OPERATOR):
            if self._current_token.value not in ('*', '/'):
                break
            token = self._current_token
            self.__check_token(TokenType.OPERATOR)
            result = BinOp(result, token, self.__factor())
        return result
    
    def __expr(self) -> BinOp:
        result = self.__term()
        while self._current_token and self._current_token.type_ == TokenType.OPERATOR:
            if self._current_token.value not in ('+', '-'):
                break
            token = self._current_token
            self.__check_token(TokenType.OPERATOR)
        
            result = BinOp(result, token, self.__term())
        return result
    
    def eval(self, s: str) -> BinOp:
        self._lexer.init(s)
        self._current_token = self._lexer.next()
        return self.__expr()
