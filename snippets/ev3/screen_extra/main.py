#!/usr/bin/env pybricks-micropython

import math

from pybricks.hubs import EV3Brick
from pybricks.parameters import Color
from pybricks.tools import wait
from pybricks.media.ev3dev import Font, Image


# Initialize the EV3
ev3 = EV3Brick()


# SPLIT SCREEN ################################################################

# Make a sub-image for the left half of the screen
left = Image(ev3.screen, sub=True, x1=0, y1=0,
             x2=ev3.screen.width // 2 - 1, y2=ev3.screen.height - 1)

# Make a sub-image for the right half of the screen
right = Image(ev3.screen, sub=True, x1=ev3.screen.width // 2, y1=0,
              x2=ev3.screen.width - 1, y2=ev3.screen.height - 1)

# Use a monospaced font so that text is vertically aligned when we print
right.set_font(Font(size=8, monospace=True))


# Graphing y = sin(x)
def f(x):
    return math.sin(x)


for t in range(200):
    # Graph on left side

    # Scale t to x-axis and compute y values
    x0 = (t - 1) * 2 * math.pi / left.width
    y0 = f(x0)
    x1 = t * 2 * math.pi / left.width
    y1 = f(x1)

    # Scale y values to screen coordinates
    sy0 = (-y0 + 1) * left.height / 2
    sy1 = (-y1 + 1) * left.height / 2

    # Shift the current graph to the left one pixel
    left.draw_image(-1, 0, left)
    # Fill the last column with white to erase the previous plot point
    left.draw_line(left.width - 1, 0, left.width - 1, left.height - 1, 1, Color.WHITE)
    # Draw the new value of the graph in the last column
    left.draw_line(left.width - 2, int(sy0), left.width - 1, int(sy1), 3)

    # Print every 10th value on right side
    if t % 10 == 0:
        right.print('{:10.2f}{:10.2f}'.format(x1, y1))

    wait(100)


# SPRITE ANIMATION ############################################################

# Copy of screen for double-buffering
buf = Image(ev3.screen)

# Load images from file
bg = Image('background.png')
sprite = Image('sprite.png')

# Number of cells in each sprite animation
NUM_CELLS = 8

# Each cell in the sprite is 75 x 100 pixels
CELL_WIDTH, CELL_HEIGHT = 75, 100

# Get sub-images for each individual cell
# This is more efficient that loading individual images
walk_right = [Image(sprite, sub=True, x1=x * CELL_WIDTH, y1=0,
                    x2=(x + 1) * CELL_WIDTH - 1, y2=CELL_HEIGHT - 1)
              for x in range(NUM_CELLS)]
walk_left = [Image(sprite, sub=True, x1=x * CELL_WIDTH, y1=CELL_HEIGHT,
                   x2=(x + 1) * CELL_WIDTH - 1, y2=2 * CELL_HEIGHT - 1)
             for x in range(NUM_CELLS)]


# Walk from left to right
for x in range(-100, 200, 2):
    # Start with the background image
    buf.draw_image(0, 0, bg)
    # Draw the current sprite - purple is treated as transparent
    buf.draw_image(x, 5, walk_right[x // 5 % NUM_CELLS], Color.PURPLE)
    # Copy the double-buffer to the screen
    ev3.screen.draw_image(0, 0, buf)
    # 20 frames per second
    wait(50)

# Walk from right to left
for x in range(200, -100, -2):
    buf.draw_image(0, 0, bg)
    buf.draw_image(x, 5, walk_left[x // 5 % NUM_CELLS], Color.PURPLE)
    ev3.screen.draw_image(0, 0, buf)
    wait(50)

wait(1000)
