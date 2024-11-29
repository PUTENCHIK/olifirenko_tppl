import pytest
from pascal import (
    Interpreter, NodeVisitor,
    BadToken, InvalidTokenOrder, InvalidFactor, TooManyDotsInNumber,
    InvalidSyntaxOfStatement, ExtraSemicolon, UnkownVariable
)


@pytest.fixture
def interpreter(scope="function") -> Interpreter:
    return Interpreter()


class TestInterpreter:
    
    def test_empty_program(self, interpreter):
        assert interpreter.eval("BEGIN END.") == dict()

    def test_bad_token(self, interpreter):
        with pytest.raises(BadToken):
            assert interpreter.eval("BEGIN , END.")
    
    def test_single_assignment(self, interpreter):
        assert interpreter.eval("BEGIN x:=1; END.")
    
    def test_multiple_assignment(self, interpreter):
        assert interpreter.eval(
            """
            BEGIN
                a := 1;
                b: = 2;
                c:=  3;
            END.
            """
        )
    
    def test_assignment_expr(self, interpreter):
        assert interpreter.eval(
            """
            BEGIN
                a := 1 + 2 / 4;
            END.
            """
        ) == {'a': 1.5}
        assert interpreter.eval(
            """
            BEGIN
                a := +-+-1;
            END.
            """
        ) == {'a': 1.0}
    
    def test_assignment_variable(self, interpreter):
        assert interpreter.eval(
            """
            BEGIN
                a := 1;
                b := a;
                a := 3;
            END.
            """
        ) == {'a': 3.0, 'b': 1.0}
    
    def test_difficult_assignment(self, interpreter):
        assert interpreter.eval(
            """
            BEGIN
                a := 1; b := -5; c := 6;
                D := b*b + 4*a*c;
            END.
            """
        ) == {'a': 1.0, 'b': -5.0, 'c': 6.0, 'D': 49}
    
    def test_complex_statements(self, interpreter):
        assert interpreter.eval(
            """
            BEGIN
                BEGIN END;
            END.
            """
        ) == dict()
        assert interpreter.eval(
            """
            BEGIN
                BEGIN
                    a:= 1;
                    BEGIN END;
                    b := 2
                END;
            END.
            """
        ) == {'a': 1, 'b': 2}
    
    def test_invalid_token_order(self, interpreter):
        with pytest.raises(InvalidTokenOrder):
            assert interpreter.eval(
                """
                BEGIN a =: 1 END.
                """
            )

    def test_invalid_factor(self, interpreter):
        with pytest.raises(InvalidFactor):
            assert interpreter.eval(
                """
                BEGIN a := 1 + END.
                """
            )

    def test_invalid_syntax_of_statement(self, interpreter):
        with pytest.raises(InvalidSyntaxOfStatement):
            assert interpreter.eval(
                """
                BEGIN 1 END.
                """
            )

    def test_extra_semicolon(self, interpreter):
        with pytest.raises(ExtraSemicolon):
            assert interpreter.eval(
                """
                BEGIN
                    BEGIN
                        a:=1;
                    END;
                END.
                """
            )

    def test_unknown_variable(self, interpreter):
        with pytest.raises(UnkownVariable):
            assert interpreter.eval(
                """
                BEGIN a := b; END.
                """
            )

    def test_too_many_dots_in_number(self, interpreter):
        with pytest.raises(TooManyDotsInNumber):
            assert interpreter.eval(
                """
                BEGIN a := 1..5; END.
                """
            )

    def test_init_node_visitor(self):
        nv = NodeVisitor()
        assert nv.visit() == None
    
    def test_parens(self, interpreter):
        assert interpreter.eval(
            """
            BEGIN
                x:= 2 + 3 * (2 + 3);
                y:= 2 / 2 - 2 + 3 * ((1 + 1) + (1 + 1));
            END.
            """
        )
    