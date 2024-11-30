from .parser import Parser
from .ast import (BinOp, Number, UnaryOp, Variable, Assignment, Statement,
                  Empty, StatementList, ComplexStatement, Program)
from .exceptions import UnkownVariable
from .namespace import Namespace


class NodeVisitor:
    
    def visit(self):
        pass
    

class Interpreter(NodeVisitor):
    
    def __init__(self) -> None:
        self._parser = Parser()
        self.namespace = None
        
    def visit(self, node):
        if isinstance(node, Number):
            return self._visit_number(node)
        
        elif isinstance(node, BinOp):
            return self._visit_binop(node)
        
        elif isinstance(node, UnaryOp):
            return self._visit_unaryop(node)
        
        elif isinstance(node, Variable):
            return self._visit_variable(node)
        
        elif isinstance(node, Assignment):
            return self._visit_assignment(node)
        
        elif isinstance(node, Statement):
            return self._visit_statement(node)
        
        elif isinstance(node, Empty):
            # return self._visit_empty(node)
            pass
        
        elif isinstance(node, StatementList):
            return self._visit_statement_list(node)
        
        elif isinstance(node, ComplexStatement):
            return self._visit_complex_statement(node)
        
        elif isinstance(node, Program):
            return self._visit_program(node)
        
        # else:
            # raise Exception(f"Unkown node in tree: {type(node).__name__}")
        
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
            # case _:
                # raise RuntimeError(f"invalid operator: {node.op.value}")
    
    def _visit_unaryop(self, node: UnaryOp) -> float:
        match node.op.value:
            case "+":
                return self.visit(node.expr)
            case "-":
                return -self.visit(node.expr)
            # case _:
                # raise RuntimeError(f"invalid unary operator: {node.op.value}")
    
    def _visit_variable(self, node: Variable) -> float:
        value = self.namespace.get(node.name.value)
        if value is None:
            raise UnkownVariable(node.name.value)
        
        return value

    def _visit_assignment(self, node: Assignment) -> None:
        self.namespace.set(node.var.value, self.visit(node.expr))

    def _visit_statement(self, node: Statement) -> None:
        self.visit(node.value)

    def _visit_statement_list(self, node: StatementList) -> None:
        self.visit(node.first)
        if node.second is not None:
            self.visit(node.second)

    def _visit_complex_statement(self, node: ComplexStatement) -> None:
        inner_namespace = Namespace(self.namespace)
        if self.namespace is not None:
            self.namespace.add_inner(inner_namespace)

        self.namespace = inner_namespace
        self.visit(node.list_)
        if self.namespace.parent is not None:
            self.namespace = self.namespace.parent

    def _visit_program(self, node: Program) -> Namespace:
        self.visit(node.comp_statement)

        return self.namespace
        
    def eval(self, code: str) -> Namespace:
        tree = self._parser.eval(code)
        self.namespace = None
        
        return self.visit(tree)
