"""
This program is for CNC Machine
(in the "Invention Squad: Broken" lesson unit).

Follow the corresponding building instructions in the LEGO® SPIKE™ Prime App.

This program will draw a rectangle.
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port


# Configure the Hub, the Force Sensor and the Motor
hub = PrimeHub()
horizontal_motor = Motor(Port.A)
vertical_motor = Motor(Port.C)

# Draw a rectangle
horizontal_motor.run_angle(speed=1000, rotation_angle=400)   # go right
vertical_motor.run_angle(speed=1000, rotation_angle=100)   # go down
horizontal_motor.run_angle(speed=1000, rotation_angle=-400)   # go left
vertical_motor.run_angle(speed=1000, rotation_angle=-100)   # go up
