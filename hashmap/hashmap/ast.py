from .token import Token


class Node:
    pass


class Condition(Node):

    def __init__(self, operator: Token, value: Token):
        self.op = operator
        self.value = value


class Value(Node):

    def __init__(self, value: Token):
        self.value = value
