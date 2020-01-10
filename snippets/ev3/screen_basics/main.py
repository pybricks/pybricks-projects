#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.resources import Image, Font
from pybricks.media.ev3dev import ImageFile

# It takes some time for fonts to load from file, so it is best to only
# load them once at the beginning of the program like this:
tiny_font = Font(size=6)
big_font = Font(size=24, bold=True)
chinese_font = Font(size=24, lang='zh-cn')

# The same goes for images
ev3_img = Image(ImageFile.EV3_ICON)


# Initialize the EV3
ev3 = EV3Brick()


# TEXT ########################################################################

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

# Wait some time too look at text
wait(5000)


# IMAGES ######################################################################

# TODO: this needs to be implemented in the Image class
def show_image(img):
    ev3.screen.clear()
    x = (ev3.screen.width - img.width) // 2
    y = (ev3.screen.height - img.height) // 2
    ev3.screen.draw_image(x, y, img)


# Show an image
show_image(ev3_img)

# Wait some time too look at image
wait(5000)


# SHAPES ######################################################################

# Clear the screen
ev3.screen.clear()

# Draw a rectangle
ev3.screen.draw_box(10, 10, 40, 40)

# Draw a solid rectangle
ev3.screen.draw_box(20, 20, 30, 30, fill=True)

# Draw a rectangle with rounded corners
ev3.screen.draw_box(50, 10, 80, 40, 5)

# Draw a circle
ev3.screen.draw_circle(25, 75, 20)

# Draw a triangle using lines
x1, y1 = 65, 55
x2, y2 = 50, 95
x3, y3 = 80, 95
ev3.screen.draw_line(x1, y1, x2, y2)
ev3.screen.draw_line(x2, y2, x3, y3)
ev3.screen.draw_line(x3, y3, x1, y1)

# Wait some time too look at shapes
wait(5000)
