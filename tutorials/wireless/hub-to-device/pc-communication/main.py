# NOTE: Run this program with the latest
# firmware provided via https://beta.pybricks.com/

from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Standard MicroPython modules
from usys import stdin, stdout
from uselect import poll

motor = Motor(Port.A)

# Optional: Register stdin for polling. This allows
# you to wait for incoming data without blocking.
keyboard = poll()
keyboard.register(stdin)

while True:

    # Optional: Check available input.
    while not keyboard.poll(0):
        # Optional: Do something here.
        wait(10)

    # Read three bytes.
    cmd = stdin.buffer.read(3)

    # Decide what to do based on the command.
    if cmd == b"fwd":
        motor.dc(50)
    elif cmd == b"rev":
        motor.dc(-50)
    elif cmd == b"bye":
        break
    else:
        motor.stop()
    
    # Send a response.
    stdout.buffer.write(b"OK")
