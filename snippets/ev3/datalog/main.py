#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import DataLog, StopWatch, wait

# Create a data log file in the project folder on the EV3 Brick.
# * By default, the file name contains the current date and time, for example:
#   log_2020_02_13_10_07_44_431260.csv
# * You can optionally specify the titles of your data columns. For example,
#   if you want to record the motor angles at a given time, you could do:
data = DataLog('time', 'angle')

# Initialize a motor and make it move
wheel = Motor(Port.B)
wheel.run(500)

# Start a stopwatch to measure elapsed time
watch = StopWatch()

# Log the time and the motor angle 10 times
for i in range(10):
    # Read angle and time
    angle = wheel.angle()
    time = watch.time()

    # Each time you use the log() method, a new line with data is added to
    # the file. You can add as many values as you like.
    # In this example, we save the current time and motor angle:
    data.log(time, angle)

    # Wait some time so the motor can move a bit
    wait(100)

# You can now upload your file to your computer
