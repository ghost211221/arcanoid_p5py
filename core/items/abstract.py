from abc import ABC, abstractclassmethod


class AbstractItem(ABC):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @abstractclassmethod
    def draw(self):
        pass

    def update(self):
        pass

class AbstractRect():
    @property
    def width(self):
        return self._w
    
    @property
    def coordinates(self):
        return {
            'x1': self._x,
            'y1': self._y,
            'x2': self._x + self._w,
            'y2': self._y,
            'x3': self._x + self._w,
            'y3': self._y + self._h,
            'x4': self._x,
            'y4': self._y + self._h,
        }