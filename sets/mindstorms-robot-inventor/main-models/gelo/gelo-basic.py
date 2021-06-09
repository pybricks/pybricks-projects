from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Direction, Port, Side, Stop
from pybricks.tools import wait


class Gelo:
    def __init__(self):
        self.hub = InventorHub()

        # Configure the leg motors
        self.front_left_leg_motor = Motor(Port.D)
        self.front_right_leg_motor = \
            Motor(Port.C,
                  positive_direction=Direction.COUNTERCLOCKWISE)
        self.rear_left_leg_motor = Motor(Port.B)
        self.rear_right_leg_motor = \
            Motor(Port.A,
                  positive_direction=Direction.COUNTERCLOCKWISE)

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
            wait(100)
            self.hub.display.off()
            wait(100)


# Initialize Gelo
gelo = Gelo()

# Activate his display
gelo.activate_display()
