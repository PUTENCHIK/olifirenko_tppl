import json
from typing import Self


class PointError(Exception):
    pass


class Point:
    def __init__(self, x: int, y: int) -> None:
        if not isinstance(x, int) or not isinstance(y, int):
            raise PointError("x, y must be integer")
        self.x = x
        self.y = y
        
    def distance(self, other: Self) -> float:
        if not isinstance(other, self.__class__):
            raise NotImplementedError
        p = self - other
        return (p.x**2 + p.y**2)**0.5
    
    def to_json(self) -> str:
        return json.dumps({
            "x": self.x,
            "y": self.y
        })
    
    @classmethod
    def from_json(cls, js: str) -> Self:
        d = json.loads(js)
        return cls(d["x"], d["y"])
    
    def is_center(self) -> bool:
        return self.x == 0 and self.y == 0
        
    def __add__(self, other: Self) -> Self:
        if not isinstance(other, self.__class__):
            raise NotImplementedError
        return self.__class__(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Self) -> Self:
        if not isinstance(other, self.__class__):
            raise NotImplementedError
        return self.__class__(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            raise NotImplementedError
        return self.x == other.x and self.y == other.y
