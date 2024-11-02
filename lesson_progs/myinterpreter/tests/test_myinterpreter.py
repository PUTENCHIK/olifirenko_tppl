import pytest
from myinterpreter import Interpreter


@pytest.fixture
def interpreter(scope="function"):
    return Interpreter()


class TestMyinterpreter:
    
    def test_add(self, interpreter):
        assert interpreter.eval("2+2") == 4
        assert interpreter.eval("2+3") == 5
        
    def test_sub(self, interpreter):
        assert interpreter.eval("2-2") == 0
        assert interpreter.eval("4-3") == 1
