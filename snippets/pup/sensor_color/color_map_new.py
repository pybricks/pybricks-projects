from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize the sensor.
sensor = ColorSensor(Port.A)

# Here we choose only red, yellow, green, and blue, and provide the hues.
hues = {
    Color.RED: 350,
    Color.YELLOW: 30,
    Color.GREEN: 110,
    Color.BLUE: 210
}

# Save the updated settings. The values dictionary is empty because we don't
# need to detect black/white in this demo application.
sensor.color_map(hues, 30, {})

# color() works as usual, but it only returns red/yellow/green/blue, or None.
# This avoids accidentally detecting black on the dark gray train tracks.
while True:
    print(sensor.color())
    wait(100)
