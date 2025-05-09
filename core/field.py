from p5 import rect, fill

from .abstracts import Singleton
from .items.abstract import AbstractRect

class Field(Singleton, AbstractRect):
    def __init__(self):
        self._w = 800
        self._h = 630
        self._x = 5
        self._y = 5

    def draw_field(self):
        fill(240, 240, 240)
        rect(self._x, self._y, self._w, self._h)