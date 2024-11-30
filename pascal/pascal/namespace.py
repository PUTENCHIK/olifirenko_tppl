from typing import Self


class Namespace:

    def __init__(self, parent: Self = None):
        self.variables = dict()
        self.parent = parent
        self.inners = list()
    
    def get(self, var: str) -> float | None:
        if var in self.variables:
            return self.variables[var]
        elif self.parent is not None:
            return self.parent.get(var)
        else:
            return None
    
    def set(self, var: str, value: float) -> None:
        self.variables[var] = value
    
    def add_inner(self, inner: Self) -> None:
        self.inners += [inner]

    def to_json(self) -> dict:
        obj = dict()
        if len(self.variables) > 0:
            obj['vars'] = self.variables
        if len(self.inners) > 0:
            inners = []
            for inner in self.inners:
                inner = inner.to_json()
                if len(inner) > 0:
                    inners += [inner]
            if len(inners) > 0:
                obj['inners'] = inners
        
        return obj
    
    def vars(self) -> dict:
        result = {}
        for inner in self.inners:
            result |= inner.vars()

        return result | self.variables
