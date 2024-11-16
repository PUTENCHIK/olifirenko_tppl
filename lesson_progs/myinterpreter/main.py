from myinterpreter import Parser, Interpreter
from pprint import pprint


v = "----++++2"
i = Interpreter()
print(i._parser.eval(v))
print(i.eval(v))
