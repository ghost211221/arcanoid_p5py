from p5 import run, size, background

from core.field import Field
from core.items.ball import Ball
from core.items.plank import Plank
from core.items.block import Block


figures = [
    Ball(100, 200),
    # Plank(200, 300),
    # Block(0, 0)
]

def update_state():
    for figure in figures:
        figure.update()

def setup():
    size(1024, 640)
    background(200, 200, 200)

def draw():
    background(200, 200, 200)
    field = Field()
    field.draw_field()

    for figure in figures:
        figure.draw()

    update_state()

run()