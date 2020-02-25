#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.iodevices import Ev3devSensor

# Initialize an Ev3devSensor.
# In this example we use the
# LEGO MINDSTORMS EV3 Color Sensor.
sensor = Ev3devSensor(Port.S3)

while True:
    # Read the raw RGB values
    r, g, b = sensor.read('RGB-RAW')

    # Print results
    print('R: {0}\t G: {1}\t B: {2}'.format(r, g, b))

    # Wait
    wait(200)
