import pytest
from hashmap import TokenType, Token, Lexer, TooManyDotsInNumber, BadOperatorToken


class TestToken:

    def test_init(self):
        token = Token(TokenType.OPERATOR, "=")
        assert str(token) == f"({TokenType.OPERATOR}: =)"


class TestLexer:

    def test_exceptions(self):
        lexer = Lexer()
        with pytest.raises(TooManyDotsInNumber):
            lexer.init("1..2")
            lexer.next()
        
        with pytest.raises(BadOperatorToken):
            lexer.init(">>")
            lexer.next()
