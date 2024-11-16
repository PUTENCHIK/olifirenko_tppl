from myinterpreter import Parser, Interpreter
from pprint import pprint


v = "0 - 1 - 2/2"
i = Interpreter()
print(i._parser.eval(v))
print(i.eval(v))
