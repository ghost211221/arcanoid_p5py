from core.abstracts import Singleton
from core.field import Field

from core.items.ball import Ball
from core.items.plank import Plank
from core.items.block import Block

class Config(Singleton):
    def __init__(self):
        self._field = Field()

        x = (self._field.coordinates['x1'] + self._field.coordinates['x2']) / 2 - 30
        y = self._field.coordinates['y3'] - 40

        self._plank = Plank(x, y)
        x = (self._plank.coordinates['x1'] + self._plank.coordinates['x2']) / 2
        y = self._plank.coordinates['y1'] - 10
        self._ball = Ball(x, y)
        self.place_ball()

        self._blocks = []

        self._ball.set_borders(self._field.coordinates)
        self._plank.set_borders(self._field.coordinates)

        self._score = 0

    @property
    def field(self):
        return self._field
    
    @property
    def ball(self):
        return self._ball

    def increase_score(self):
        self._score += 1

    @property
    def score(self):
        return self._score
    
    def init_score(self):
        self._score = 0

    def place_plank(self):
        x = (self._field.coordinates['x1'] + self._field.coordinates['x2']) / 2 - self._plank.width / 2
        y = self._field.coordinates['y3'] - 40
        self._plank.set_coords(x, y)

    def place_ball(self):
        xm = (self._plank.coordinates['x1'] + self._plank.coordinates['x2']) / 2
        y = self._plank.coordinates['y1'] - self._ball._radius
        self._ball.set_coords(xm, y)

    @property
    def figures(self):
        return [self._ball, self._plank] + self._blocks