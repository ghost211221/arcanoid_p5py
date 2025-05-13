from math import pi, cos, sin
from p5 import circle, fill

from .abstract import AbstractItem


class Ball(AbstractItem):
    def __init__(self, x,y):
        super().__init__(x, y)

        self._radius = 10
        self._speed = 0
        self._alpha = 45

        self._vx = self._speed * cos(self._alpha * pi / 180)
        self._vy = self._speed * sin(self._alpha * pi / 180)

        self._xb1 = None
        self._xb2 = None
        self._yb1 = None
        self._yb2 = None

    @property
    def speed(self):
        return self._speed
    
    def set_speed(self, value):
        self._speed = value
        self._vx = self._speed * cos(self._alpha * pi / 180)
        self._vy = -1 * self._speed * sin(self._alpha * pi / 180)

        
    def set_borders(self, coords_dict: dict) -> None:
        self._xb1 = coords_dict['x1']
        self._xb2 = coords_dict['x2']
        self._yb1 = coords_dict['y1']
        self._yb2 = coords_dict['y3']

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def draw(self):
        fill(215, 0, 0)
        circle(self._x, self._y, self._radius, mode='RADIUS')

    def update(self):
        if (self._x + self._radius) >= self._xb2 or (self._x - self._radius) <= self._xb1:
            self._vx *= -1

        if (self._y + self._radius) >= self._yb2 or (self._y - self._radius) <= self._yb1:
            self._vy *= -1

        self._x += self._vx
        self._y += self._vy
    
