#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.customdevices import I2CDevice
from pybricks.tools import wait, print

# Initialize the EV3
ev3 = EV3Brick()

# Initialize I2C Sensor
gyro = I2CDevice(ev3.Port.S2, 0xD2 >> 1)

# Check the Who Am I register
if 211 not in gyro.read(0x0F, 1):
    raise OSError("Device is not attached")

# Register values and config routine for dIMU (Thanks to Botbench)
DIMU_GYRO_RANGE_250 = 0x00  # 250 dps range
DIMU_GYRO_CTRL_REG1 = 0x20  # CTRL_REG1 for Gyro
DIMU_GYRO_CTRL_REG2 = 0x21  # CTRL_REG2 for Gyro
DIMU_GYRO_CTRL_REG3 = 0x22  # CTRL_REG3 for Gyro
DIMU_GYRO_CTRL_REG4 = 0x23  # CTRL_REG4 for Gyro
DIMU_GYRO_CTRL_REG5 = 0x24  # CTRL_REG5 for Gyro
DIMU_GYRO_ALL_AXES = 0x28 + 0x80  # All Axes for Gyro
REG4VAL = bytes((DIMU_GYRO_RANGE_250 + 0x80, ))

# Configure the gyro sensor (Thanks to Botbench)
gyro.write(DIMU_GYRO_CTRL_REG2, b'\x00')
gyro.write(DIMU_GYRO_CTRL_REG3, b'\x08')
gyro.write(DIMU_GYRO_CTRL_REG4, REG4VAL)
gyro.write(DIMU_GYRO_CTRL_REG5, b'\x00')
gyro.write(DIMU_GYRO_CTRL_REG1, b'\x0F')


# Convert two bytes into a signed integer
def get_int(msb, lsb):
    a = lsb + (msb << 8)
    return a if a < 2**15 else a-2**16


while True:
    # Read 6 bytes from the sensor
    y_l, y_h, x_l, x_h, z_l, z_h = gyro.read(DIMU_GYRO_ALL_AXES, 6)

    # Get rate value for each axis
    x = get_int(x_h, x_l)
    y = get_int(y_h, y_l)
    z = get_int(z_h, z_l)

    # Print results and wait
    print(x, y, z)
    wait(500)
