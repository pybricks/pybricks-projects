from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.geometry import Axis
from pybricks.parameters import Direction, Port, Side, Stop
from pybricks.tools import wait


class Gelo:
    def __init__(self):
        self.hub = InventorHub(top_side=Axis.Z, front_side=-Axis.X)

        # Configure the leg motors
        self.front_left_leg_motor = Motor(Port.D)
        self.front_right_leg_motor = \
            Motor(Port.C,
                  positive_direction=Direction.COUNTERCLOCKWISE)
        self.rear_left_leg_motor = Motor(Port.B)
        self.rear_right_leg_motor = \
            Motor(Port.A,
                  positive_direction=Direction.COUNTERCLOCKWISE)
        self.leg_motors = [
            self.front_left_leg_motor, self.front_right_leg_motor,
            self.rear_left_leg_motor, self.rear_right_leg_motor
        ]

        # Configure the sensors
        self.color_sensor = ColorSensor(Port.F)
        self.distance_sensor = UltrasonicSensor(Port.E)

    def activate_display(self):
        self.hub.display.orientation(up=Side.TOP)

        for _ in range(10):
            self.hub.display.image(
                image=[[00, 11, 33, 11, 00],
                       [11, 33, 33, 33, 11],
                       [33, 66, 99, 66, 33],
                       [11, 33, 66, 33, 11],
                       [00, 11, 33, 11, 00]])
            wait(50)
            self.hub.display.off()
            wait(50)

    def straighten_legs(self):
        for leg_motor in self.leg_motors:
            leg_motor.run_target(
                speed=1000,
                target_angle=0,
                wait=False)

    def walk(self, speed: int, seconds: int):
        for _ in range(seconds):
            self.front_left_leg_motor.run_time(speed=speed,
                                               time=500,
                                               wait=False)
            self.rear_right_leg_motor.run_time(speed=speed,
                                               time=500)

            self.front_right_leg_motor.run_time(speed=speed,
                                                time=500,
                                                wait=False)
            self.rear_left_leg_motor.run_time(speed=speed,
                                              time=500)


# Initialize Gelo
gelo = Gelo()

# Straighten his legs
gelo.straighten_legs()

# Turn on his Distance Sensor
gelo.distance_sensor.lights.on(100)

# Activate his display
gelo.activate_display()

# Gelo takes his first walk
gelo.walk(speed=800, seconds=10)

# Turn off his Distance Sensor
gelo.distance_sensor.lights.off()
