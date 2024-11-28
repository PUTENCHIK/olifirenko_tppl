from .token import Token


class Node:
    pass


class Number(Node):
    def __init__(self, token: Token) -> None:
        self.token = token
        
    def __str__(self) -> str:
        return f"{self.token}"


class BinOp(Node):
    
    def __init__(self, left: Node, op: Token, right: Node) -> None:
        self.left = left
        self.op = op
        self.right = right
        
    def __str__(self) -> str:
        return f"({self.left} {self.op.value} {self.right})"


class UnaryOp(Node):
    
    def __init__(self, op: Token, expr: Node) -> None:
        self.op = op
        self.expr = expr
        
    def __str__(self) -> str:
        return f"({self.op}{self.expr})"


class Variable(Node):

    def __init__(self, name: Token):
        self.name = name

    def __str__(self) -> str:
        return f"{__class__.__name__}({self.name})"
    

class Assignment(Node):

    def __init__(self, var: Token, expr: Node):
        self.var = var
        self.expr = expr

    def __str__(self) -> str:
        return f"{__class__.__name__}({self.var} := {self.expr})"
    

class Statement(Node):

    def __init__(self, value: Node):
        self.value = value

    def __str__(self) -> str:
        return f"{__class__.__name__}({self.value})"
    
class Empty(Node):
    
    def __init__(self):
        pass

    def __str__(self) -> str:
        return f"{__class__.__name__}"
