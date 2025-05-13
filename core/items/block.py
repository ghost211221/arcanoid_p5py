from p5 import rect, fill

from .abstract import AbstractItem, AbstractRect

class Block(AbstractItem, AbstractRect):
    def __init__(self, x, y):
        super().__init__(x, y)

        self._w = 40
        self._h = 20
        self._health = 1

    def draw(self):
        if self._health > 0:
            fill(75, 50, 220)
            rect(self._x, self._y, self._w, self._h)
        