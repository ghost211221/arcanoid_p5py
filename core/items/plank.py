from p5 import rect, fill

from core.abstracts import Singleton
from .abstract import AbstractItem, AbstractRect

class Plank(AbstractItem, AbstractRect, Singleton):
    def __init__(self, x, y):
        super().__init__(x, y)

        self._w = 120
        self._h = 10

    def draw(self):
        fill(215, 50, 0)
        rect(self._x, self._y, self._w, self._h)
        