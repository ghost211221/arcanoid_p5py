from math import pi, cos, sin
from p5 import circle, fill

from core.abstracts import Singleton
from .abstract import AbstractItem
from core.field import Field


f = Field()

class Ball(AbstractItem):
    def __init__(self, x,y):
        super().__init__(x, y)

        self._radius = 10
        self._speed = 10
        self._alpha = 45

        self._vx = self._speed * cos(self._alpha * pi / 180)
        self._vy = self._speed * sin(self._alpha * pi / 180)

    def draw(self):
        fill(215, 0, 0)
        circle(self._x, self._y, self._radius)

    def update(self):
        xb1 = f.coordinates['x1']
        xb2 = f.coordinates['x2']
        yb1 = f.coordinates['y1']
        yb2 = f.coordinates['y3']
        
        if (self._x + self._radius) >= xb2 or (self._x - self._radius) <= xb1:
            self._vx *= -1

        if (self._y + self._radius) >= yb2 or (self._y - self._radius) <= yb1:
            self._vy *= -1

        self._x += self._vx
        self._y += self._vy
    
