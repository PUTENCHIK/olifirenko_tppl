import pytest
from myinterpreter import Interpreter


@pytest.fixture
def interpreter(scope="function") -> Interpreter:
    return Interpreter()


class TestMyinterpreter:
    
    def test_add(self, interpreter):
        assert interpreter.eval("2+2") == 4
        assert interpreter.eval("2+3") == 5
        
    def test_sub(self, interpreter):
        assert interpreter.eval("2-2") == 0
        assert interpreter.eval("4-3") == 1
        
    def test_spaces(self, interpreter):
        assert interpreter.eval("   2   -  2  ") == 0
        
    def test_int(self, interpreter):
        assert interpreter.eval("22+22") == 44
        assert interpreter.eval("14 + 16") == 30
    
    def test_float(self, interpreter):
        assert interpreter.eval("1.5 + 1.5") == 3
        assert interpreter.eval("0.99 + 0.01") == 1
        
    def test_float_error(self, interpreter):
        with pytest.raises(SyntaxError):
            assert interpreter.eval("0..99 + 0.01") == 1
            assert interpreter.eval("0.99 + 0.01.") == 1
            
    def test_mul(self, interpreter):
        assert interpreter.eval("5 * 2") == 10
        assert interpreter.eval("2.5 * 2") == 5
        assert interpreter.eval("6 * 0") == 0
    
    def test_div(self, interpreter):
        assert interpreter.eval("5 / 2") == 2.5
        assert interpreter.eval("1 / 4") == 0.25
        assert interpreter.eval("0 / 1") == 0
            
    def test_term(self, interpreter):
        assert interpreter.eval("2+2-2") == 2
        assert interpreter.eval("7 + 2 - 1") == 8
        assert interpreter.eval("2 + 2 * 2") == 6
        assert interpreter.eval("10 / 2 + 10 * 0.5") == 10
        assert interpreter.eval("8 / 2 / 2 * 4 - 7 * 0.5 * 2") == 1
    
    def test_brackets(self, interpreter):
        assert interpreter.eval("(2 + 2)") == 4
        assert interpreter.eval("((((2))))") == 2
        assert interpreter.eval("( ((  (  2)   ))  )") == 2
        assert interpreter.eval("(2 + 2) * 2") == 8
        assert interpreter.eval("(2 + (2 * (3 + 5)))") == 18
        
    def test_brackets_error(self, interpreter):
        with pytest.raises(SyntaxError):
            assert interpreter.eval("(2") == 2
            assert interpreter.eval("2)") == 2
        
    # def test_null(self, interpreter):
    #     assert interpreter.eval("") == None
