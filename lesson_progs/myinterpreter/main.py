from myinterpreter import Parser


p = Parser()
print(p.eval("2 * (2 - 1 * (12 - 9))"))