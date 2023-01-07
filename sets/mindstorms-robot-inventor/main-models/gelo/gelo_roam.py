from pybricks.parameters import Icon
from urandom import choice
from gelo import Gelo

with Gelo() as gelo:
    # If the ultrasonic sensor measures less than
    # 30 cm (1 ft), then we are too close!
    def too_close():
        return gelo.ultrasonic.distance() < 300

    while True:
        # walk until the ultrasonic sensor detects an obstruction
        gelo.hub.display.icon(Icon.ARROW_UP)
        gelo.walk_until(too_close)

        # randomly turn left or right to avoid the obstruction
        direction = choice(["left", "right"])

        if choice == "left":
            gelo.hub.display.icon(Icon.ARROW_LEFT)
            gelo.walk(steer=90, time=4000)
        else:
            gelo.hub.display.icon(Icon.ARROW_RIGHT)
            gelo.walk(steer=-90, time=4000)
