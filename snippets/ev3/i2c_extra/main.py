#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import I2CDevice
from pybricks.parameters import Port

# Initialize the EV3
ev3 = EV3Brick()

# Initialize I2C Sensor
device = I2CDevice(Port.S2, 0xD2 >> 1)

# Recommended for reading
result, = device.read(reg=0x0F, length=1)

# Read 1 byte from no particular register:
device.read(reg=None, length=1)

# Read 0 bytes from no particular register:
device.read(reg=None, length=0)

# I2C write operations consist of a register byte followed
# by a series of data bytes. Depending on your device, you
# can choose to skip the register or data as follows:

# Recommended for writing:
device.write(reg=0x22, data=b'\x08')

# Write 1 byte to no particular register:
device.write(reg=None, data=b'\x08')

# Write 0 bytes to a particular register:
device.write(reg=0x08, data=None)

# Write 0 bytes to no particular register:
device.write(reg=None, data=None)
