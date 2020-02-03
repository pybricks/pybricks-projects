#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import I2CDevice
from pybricks.parameters import Port

# Initialize the EV3
ev3 = EV3Brick()

# Initialize I2C Sensor
device = I2CDevice(Port.S2, 0xD2 >> 1)

# Read one byte from the device.
# For this device, we can read the Who Am I
# register (0x0F) for the expected value: 211.
if 211 not in device.read(0x0F):
    raise OSError("Device is not attached")

# To write data, create a bytes object of one
# or more bytes. For example:
# data = bytes((1, 2, 3))

# Write one byte (value 0x08) to register 0x22
device.write(0x22, bytes((0x08,)))
