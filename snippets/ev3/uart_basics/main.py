#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import print
from pybricks.iodevices import UARTDevice
from pybricks.media.ev3dev import SoundFile

# Initialize the EV3
ev3 = EV3Brick()

# Initialize sensor port 2 as a uart device
ser = UARTDevice(ev3.Port.S2, baudrate=115200)

# Write some data
ser.write(b'\r\nHello, world!\r\n')

# Play a sound while we wait for some data
for i in range(3):
    ev3.speaker.play(SoundFile.HELLO)
    ev3.speaker.play(SoundFile.GOOD)
    ev3.speaker.play(SoundFile.MORNING)
    print("Bytes waiting to be read:", ser.waiting())

# Read all data received while the sound was playing
data = ser.read_all()
print(data)
