from .parser import Parser
from .ast import Number, BinOp, UnaryOp


class NodeVisitor:
    
    def visit(self):
        pass
    

class Interpreter(NodeVisitor):
    
    def __init__(self) -> None:
        self._parser = Parser()
        
    def visit(self, node):
        if isinstance(node, Number):
            return self._visit_number(node)
        elif isinstance(node, BinOp):
            return self._visit_binop(node)
        elif isinstance(node, UnaryOp):
            return self._visit_unaryop(node)
        
    def _visit_number(self, node: Number) -> float:
        return float(node.token.value)
    
    def _visit_binop(self, node: BinOp) -> float:
        match node.op.value:
            case "+":
                return self.visit(node.left) + self.visit(node.right)
            case "-":
                return self.visit(node.left) - self.visit(node.right)
            case "*":
                return self.visit(node.left) * self.visit(node.right)
            case "/":
                return self.visit(node.left) / self.visit(node.right)
            case _:
                raise RuntimeError(f"invalid operator: {node.op.value}")
    
    def _visit_unaryop(self, node: UnaryOp) -> float:
        match node.op.value:
            case "+":
                return self.visit(node.expr)
            case "-":
                return -self.visit(node.expr)
            case _:
                raise RuntimeError(f"invalid unary operator: {node.op.value}")
        
    def eval(self, code: str) -> float:
        tree = self._parser.eval(code)
        
        return self.visit(tree)
