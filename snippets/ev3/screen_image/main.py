#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.media.ev3dev import Image, ImageFile

# It takes some time to load images from the SD card, so it is best to load
# them once at the beginning of a program like this:
ev3_img = Image(ImageFile.EV3_ICON)


# Initialize the EV3
ev3 = EV3Brick()


# Show an image
ev3.screen.load_image(ev3_img)

# Wait some time to look at the image
wait(5000)
