#Author: Ikenna
#Date: 10/24/2023
#Purpose: Assignment 12

from system import *
from body import *

WINDOW_SIZE = 400
PIXEL_PER_METER = 7 / 1e10


FRAMERATE = 30
TIMESTEP = 1.0/FRAMERATE
TIMESCALE = 3.0e6

sun = Body(1.98892e30, 0, 0, 0, 0, 20, 1, 1, 0)
mercury = Body(0.330e24, -57.9e9, 0, 0, 47890, 3, 1, 0, 0 )
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 9, 1, 1, 1)
earth = Body(5.97e24, -149.6e9,0,0,29790,10, 0, 0, 1)
mars = Body(0.642e24, -228.0e9, 0, 0, 24140, 5, 0, 1, 0)

solar = System([sun, mercury, venus, earth, mars])

def mydraw():

    set_clear_color(0, 0, 0)  # black background
    clear()

    solar.draw(WINDOW_SIZE/2, WINDOW_SIZE/2, PIXEL_PER_METER)

    solar.update(TIMESTEP * TIMESCALE)

start_graphics(mydraw, height = WINDOW_SIZE, width = WINDOW_SIZE, framerate = FRAMERATE)