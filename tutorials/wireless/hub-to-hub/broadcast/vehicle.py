from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.experimental import Broadcast

# Initialize broadcast with two topics.
radio = Broadcast(topics=["tilt", "distance"])

# Initialize the drive base.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Initialize the distance sensor.
sensor = UltrasonicSensor(Port.C)

while True:

    # Receive tilt data
    data = radio.receive("tilt")

    # If we received it, start driving.
    if data:
        pitch, roll = data
        drive_base.drive(speed=pitch * 8, turn_rate=roll * 3)
    else:
        print(data)
        drive_base.stop()


    # Send the distance data
    radio.send("distance", sensor.distance())

    # Wait some time.
    wait(50)
