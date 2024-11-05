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

    # @classmethod
    # def calc_prefix_notation(cls, s: str) -> float:
    #     tokens = cls.to_infix_notation(s).split()
    #     first, operator, second = None, None, None

    #     result = None
    #     for token in tokens:
    #         if token in cls.oprs:
    #             operator = token
    #         else:
    #             if first is None:
    #                 first = float(token)
    #             else:
    #                 second = float(token)
            
    #         if second is not None:
    #             if result is None:
    #                 result = first
                
    #             match operator:
    #                 case "+":
    #                     result += second
    #                 case "-":
    #                     result -= second
    #                 case "*":
    #                     result *= second
    #                 case _:
    #                     result /= second
    #             second = None
        
    #     return result
