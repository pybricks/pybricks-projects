def wait_for_button(ev3):
    """
    This function shows a picture of the buttons on the EV3 screen.

    Then it waits until you press a button.

    It returns which button was pressed.
    """

    # Show a picture of the buttons on the screen.
    ev3.screen.load_image('buttons.png')

    # Tip: add text or icons to the image to help you
    # remember what each button will do in your program.

    # Wait for a single button to be pressed and save the result.
    pressed = []
    while len(pressed) != 1:
        pressed = ev3.buttons.pressed()
    button = pressed[0]

    # Print which button was pressed
    ev3.screen.draw_text(2, 100, button)

    # Now wait for the button to be released.
    while any(ev3.buttons.pressed()):
        pass

    # Return which button was pressed.
    return button
