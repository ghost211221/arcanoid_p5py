from p5 import *

from .abstract import AbstractItem, AbstractRect

class Plank(AbstractItem, AbstractRect):
    def __init__(self, x, y):
        super().__init__(x, y)

        self._w = 120
        self._h = 10

        self._xb1 = None
        self._xb2 = None
        
    def set_borders(self, coords_dict: dict) -> None:
        self._xb1 = coords_dict['x1']
        self._xb2 = coords_dict['x2']

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def draw(self):
        fill(215, 50, 0)
        rect(self._x, self._y, self._w, self._h)

    def update(self):
        if mouse_x - pmouse_x:
            if (mouse_x - self._w) <= self._xb1:
                self._x = self._xb1
            elif (mouse_x + self._w) >= self._xb2:
                self._x = self._xb2 - self._w
            else:
                self._x = mouse_x
