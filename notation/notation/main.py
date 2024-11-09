from warnings import warn
from queue import Queue


class Notations:
    oprs = "+-*/"

    @classmethod
    def to_infix_notation(cls, s: str) -> str:
        operators, operands = Queue(), Queue()
        tokens = s.strip().split()
        result = []
        for token in tokens:
            q = operators if token in cls.oprs else operands
            q.put(token)

            if not operators.empty() and operands.qsize() == 2:
                result += [operands.get(), operators.get()]

        if not operands.empty():
            result += [operands.get()]
        
        if operators.qsize():
            warn(f"There are extra operators: {list(operators.queue)}")
        if operands.qsize():
            warn(f"There are extra operands: {list(operands.queue)}")
        
        return " ".join(result)
