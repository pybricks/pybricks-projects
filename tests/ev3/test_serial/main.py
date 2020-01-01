#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import print
from pybricks.iodevices import UARTDevice

# Initialize the EV3
ev3 = EV3Brick()

print("Init test")

# Initialize all ports as serial, with various init choices
ser = UARTDevice(ev3.Port.S1, 115200, 1000)
ser = UARTDevice(ev3.Port.S2, baudrate=115200, timeout=1000)
ser3 = UARTDevice(ev3.Port.S3, baudrate=115200, timeout=None)
ser4 = UARTDevice(ev3.Port.S4, 115200, 0)

print("Read test")

# Try read method, catch timeout
try:
    ser.read()
except OSError as e:
    print("timed out waiting for data", e)

ser.read(length=0)

try:
    ser.read(1)
except OSError:
    pass

# Try read all
ser.read_all()

# Try clear
ser.clear()

# How many bytes are waiting to be read?
print("Waiting bytes:", ser.waiting())

print("Write test")

# Write data
ser.waiting()
ser.write('Hi')
ser.write(b'Hello')
ser.write(chr(65))

print("Echo device starting")

# Act as an echo device until ctrl+c received
while True:
    data = ser.read_all()
    ser.write(data)

    if b'\x03' in data:
        break

ser.write(b'\r\nHanging up\r\n')
