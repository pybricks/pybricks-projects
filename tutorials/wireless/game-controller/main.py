from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

from pybricks.hubs import PrimeHub
import micropython

# Standard MicroPython modules
from usys import stdin, stdout
from uselect import poll

rwheel = Motor(Port.C, Direction.COUNTERCLOCKWISE)
lwheel = Motor(Port.A)

# Optional: Register stdin for polling. This allows
# you to wait for incoming data without blocking.
keyboard = poll()
keyboard.register(stdin)


hub = PrimeHub()

# We are receiving binary date; disable CTRL+C
micropython.kbd_intr(-1)

while True:
    # Optional: Check available input.
    while not keyboard.poll(0):
        # Optional: Do something here.
        wait(10)

    # Read three bytes.
    cmd = stdin.buffer.read(3)

    code = cmd[0]
    type_ = cmd[1]
    value = cmd[2]
    
    if code == 1 and type_ == 3:
        lwheel.run((value - 128)/128 * 1000)
    elif code == 5 and type_ == 3:
        rwheel.run((value - 128)/128 * 1000)
