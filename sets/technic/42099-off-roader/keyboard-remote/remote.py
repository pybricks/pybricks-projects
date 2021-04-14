# Import required MicroPython libraries.
from usys import stdin
from uselect import poll

# Register the standard input so we can read keyboard presses.
keyboard = poll()
keyboard.register(stdin)

while True:
    # Check if a key has been pressed.
    if keyboard.poll(0):
        
        # Read the key and print it.
        key = stdin.read(1)
        print("You pressed:", key)
