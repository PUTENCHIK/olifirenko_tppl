import pytest
from pascal import Parser


@pytest.fixture
def parser(scope="function") -> Parser:
    return Parser()


class TestAst:

    def test_str(self, parser):
        assert str(parser.eval(
            """
            BEGIN
                y: = -2;
                BEGIN
                    a := 3;
                    a := a;
                    b := 10 + a + 10 * y / 4;
                    c := a - b
                END;
                x := 11;
            END.
            """
        ))
    
    def test_str_empty(self, parser):
        assert str(parser.eval(
            """
            BEGIN
            END.
            """
        ))
