import operator

from .parser import Parser
from .ast import Condition, Value


class Iloc:
    
    def __init__(self, keys, values):
        self.__keys = keys
        self.__values = values

    def __getitem__(self, index: int):
        if not isinstance(index, int):
            raise AttributeError("HashMap.iloc keys must be integers only")
        
        items = list()
        for k, v in zip(list(self.__keys), list(self.__values)):
            items += [[k, v]]
        items = sorted(items)

        for i, (k, v) in enumerate(items):
            if i == index:
                return v
        
        raise KeyError(f"No such key: {index}")


class Ploc:

    ops = {
        '=': operator.eq,
        '<>': operator.ne,
        '>': operator.gt,
        '>=': operator.ge,
        '<': operator.lt,
        '<=': operator.le,
    }
    
    def __init__(self, keys, values):
        self.__keys = keys
        self.__values = values
        self.__parser = Parser()

    def match(self, condition: Condition, value: Value) -> bool:
        cond_value = float(condition.value.value)
        op = condition.op.value
        value = float(value.value.value)

        # print(cond_value, op, value)
        
        return Ploc.ops[op](value, cond_value)
            

    def __getitem__(self, key) -> dict:
        if not isinstance(key, str):
            raise AttributeError("HashMap.ploc keys must be strings only")

        mask = self.__parser.get_conditions(key)
        result = dict()
        for k, v in zip(list(self.__keys), list(self.__values)):
            if isinstance(k, str):
                values = self.__parser.get_values(k)

                if len(mask) == len(values):
                    # print([str(m) for m in mask], " --> ", [str(v) for v in values])
                    matching = True
                    for condition, value in zip(mask, values):
                        if not self.match(condition, value):
                            matching = False
                            break
                    if matching:
                        result[k] = v
        return result


class HashMap(dict):

    def __init__(self, mapping=None):
        if mapping is None:
            mapping = dict()
        super().__init__(mapping)

        self.__iloc = Iloc(self.keys(), self.values())
        self.__ploc = Ploc(self.keys(), self.values())
    
    @property
    def iloc(self) -> Iloc:
        return self.__iloc
    
    @property
    def ploc(self) -> Ploc:
        return self.__ploc
