#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.media.ev3dev import Font

# It takes some time for fonts to load from file, so it is best to only
# load them once at the beginning of the program like this:
tiny_font = Font(size=6)
big_font = Font(size=24, bold=True)
chinese_font = Font(size=24, lang='zh-cn')


# Initialize the EV3
ev3 = EV3Brick()


# Say hello
ev3.screen.print('Hello!')

# Say tiny hello
ev3.screen.set_font(tiny_font)
ev3.screen.print('hello')

# Say big hello
ev3.screen.set_font(big_font)
ev3.screen.print('HELLO')

# Say Chinese hello
ev3.screen.set_font(chinese_font)
ev3.screen.print('你好')

# Wait some time to look at the screen
wait(5000)
