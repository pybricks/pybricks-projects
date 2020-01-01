#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import I2CDevice

# Initialize the EV3
ev3 = EV3Brick()

# Initialize I2C Sensor
device = I2CDevice(ev3.Port.S2, 0xD2 >> 1)

# Recommended for reading
result, = device.read(reg=0x0F, length=1)

# Read 1 byte from no particular register:
device.read(reg=None, length=1)

# Read 0 bytes from no particular register:
device.read(reg=None, length=0)

# Recommended for writing:
device.write(reg=0x22, data=b'\x08')

# Write 1 byte to no particular register:
device.write(reg=None, data=b'\x08')

# Write 0 bytes to no particular register:
device.write(reg=None, data=b'')
