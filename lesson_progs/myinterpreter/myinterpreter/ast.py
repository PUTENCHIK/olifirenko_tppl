from .token import Token


class Node:
    pass


class Number(Node):
    
    def __init__(self, token: Token) -> None:
        self.token = token
        
    def __str__(self) -> str:
        # return f"{self.__class__.__name__} ({self.token})"
        return f"{self.token}"
    
    
class BinOp(Node):
    
    def __init__(self, left: Node, op: Token, right: Node) -> None:
        self.left = left
        self.op = op
        self.right = right
        
    def __str__(self) -> str:
        # return f"{self.__class__.__name__}{self.op.value}({self.left}, {self.right})"
        # return f"{self.__class__.__name__}({self.left} {self.op.value} {self.right})"
        return f"({self.left} {self.op.value} {self.right})"


class UnaryOp(Node):
    
    def __init__(self, op: Token, expr: Node) -> None:
        self.op = op
        self.expr = expr
        
    def __str__(self) -> str:
        return f"({self.op}{self.expr})"
