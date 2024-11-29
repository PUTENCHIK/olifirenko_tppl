import pytest
from pascal import (
    Token, TokenType,
    Number, BinOp, UnaryOp, Variable, Assignment, Statement,
    Empty, StatementList, ComplexStatement, Program, Node
)


class TestAst:

    def test_nodes_str(self):
        num = Number(Token(TokenType.NUMBER, 1))
        op = Token(TokenType.OPERATOR, "+")
        var = Variable(Token(TokenType.VARIABLE, 'a'))
        assign = Assignment(var, num)
        statement = Statement(assign)
        st_list = StatementList(statement, None)
        com_state = ComplexStatement(st_list)
        program = Program(com_state)
        empty = Empty()

        assert str(num)
        assert str(BinOp(num, op, num))
        assert str(UnaryOp(op, num))
        assert str(var)
        assert str(assign)
        assert str(statement)
        assert str(st_list)
        assert str(com_state)
        assert str(program)
        assert str(empty)
