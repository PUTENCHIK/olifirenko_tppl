from .token import TokenType
from .lexer import Lexer
from .ast import (BinOp, Number, UnaryOp, Variable, Assignment, Statement,
                  Empty, StatementList, ComplexStatement, Program)
from .exceptions import InvalidTokenOrder, InvalidFactor, InvalidSyntaxOfStatement, ExtraSemicolon


class Parser():
    
    def __init__(self) -> None:
        self._current_token = None
        self._lexer = Lexer()
    
    def __check_token(self, type_: TokenType) -> None:
        if self._current_token.type_ == type_:
            self._current_token = self._lexer.next()
        else:
            raise InvalidTokenOrder(str(type_), str(self._current_token.type_))
        
    def __variable(self):
        token = self._current_token
        self.__check_token(TokenType.VARIABLE)
        return token

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
        elif token.type_ == TokenType.VARIABLE:
            self.__check_token(TokenType.VARIABLE)
            return Variable(token)
        else:
            raise InvalidFactor(str(token))
        
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
    
    def __assignment(self) -> Assignment:
        var = self.__variable()
        self.__check_token(TokenType.COLON)
        self.__check_token(TokenType.EQUAL)
        expr = self.__expr()
        return Assignment(var, expr)
    
    def __statement(self) -> Statement:
        token = self._current_token

        if token.type_ == TokenType.VARIABLE:
            return Statement(self.__assignment())
        elif token.type_ == TokenType.BEGIN:
            return Statement(self.__complex_statement(False))
        elif token.value == "" or token.type_ == TokenType.END:
            return Statement(Empty())
        else:
            raise InvalidSyntaxOfStatement
        
    def __statement_list(self, expects_last_semicolon: bool):
        result = self.__statement()
        if isinstance(result.value, Empty):
            return result
        
        if expects_last_semicolon:
            self.__check_token(TokenType.SEMICOLON)
        else:
            if self._current_token.type_ == TokenType.END:
                return result
            else:
                self.__check_token(TokenType.SEMICOLON)
                if self._current_token.type_ == TokenType.END:
                    raise ExtraSemicolon()

        while self._current_token.type_ not in (TokenType.EOL, TokenType.END):
            second = self.__statement_list(expects_last_semicolon)
            result = StatementList(result, second)
        
        return result
    

    def __complex_statement(self, expects_last_semicolon: bool) -> ComplexStatement:
        variables = {}
        self.__check_token(TokenType.BEGIN)
        result = self.__statement_list(expects_last_semicolon)
        self.__check_token(TokenType.END)
        
        return ComplexStatement(result)
    

    def __program(self) -> Program:
        comp = self.__complex_statement(True)
        self.__check_token(TokenType.DOT)
        self.__check_token(TokenType.EOL)

        return Program(comp)

    
    def eval(self, s: str) -> BinOp:
        self._lexer.init(s)
        self._current_token = self._lexer.next()

        return self.__program()
