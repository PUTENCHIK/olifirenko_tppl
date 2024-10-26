import pytest
from myinterpreter import Interpreter


@pytest.fixture
def interpreter(scope="function"):
    return Interpreter()


class TestMyinterpreter:
    
    def test_add(self, interpreter):
        assert interpreter.eval("2+2") == 4
