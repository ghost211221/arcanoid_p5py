from p5 import *

from core.config import Config


c = Config()

def update_state():
    for figure in c.figures:
        figure.update()

    if c.ball.speed == 0:
        c.place_ball()

    if mouse_is_pressed:
        c.ball.set_speed(10)

def setup():
    size(1024, 640)
    background(200, 200, 200)

def draw():
    background(200, 200, 200)
    c.field.draw_field()

    for figure in c.figures:
        figure.draw()

    update_state()

run()