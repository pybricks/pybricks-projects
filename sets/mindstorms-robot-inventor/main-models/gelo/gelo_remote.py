from pybricks.hubs import InventorHub
from pybricks.pupdevices import Remote
from pybricks.parameters import Button, Color
from pybricks.tools import wait, StopWatch

from gelo import Gelo, copy_sign


#######################################################
# State management
#######################################################

_SPEED_MAP = {
    0: 0,
    1: 100,
    2: 300,
    3: 500,
    4: 800,
}

_STEER_MAP = {
    0: 0,
    1: 23,
    2: 45,
    3: 68,
    4: 90,
}


class State:
    def __init__(self):
        self.speed_index = 0
        self.steer_index = 0
        self.timer = StopWatch()

    def speed(self):
        return copy_sign(_SPEED_MAP[abs(self.speed_index)], self.speed_index)

    def steer(self):
        return copy_sign(_STEER_MAP[abs(self.steer_index)], self.steer_index)

    def inc_speed(self):
        if self.speed_index < 4:
            self.speed_index += 1

    def dec_speed(self):
        if self.speed_index > -4:
            self.speed_index -= 1

    def inc_steer(self):
        if self.steer_index < 4:
            self.steer_index += 1

    def dec_steer(self):
        if self.steer_index > -4:
            self.steer_index -= 1


#######################################################
# Helper functions
#######################################################

def pressed_oneshot_gen(remote: Remote):
    """
    Yields a list of buttons that were pressed
    since the last iteration.
    """
    previous = ()

    while True:
        pressed = remote.buttons.pressed()
        oneshot = []

        for b in pressed:
            if b not in previous:
                oneshot.append(b)

        yield oneshot

        previous = pressed


def handle_pressed(buttons: list[Button], state: State) -> bool:
    """
    Updates the state based on any new button presses.

    Returns: True if the state changed, otherwise false.
    """
    # Prefer stopping if multiple buttons are pressed
    # at the same time.
    if Button.LEFT in buttons or Button.RIGHT in buttons:
        state.speed_index = 0
        state.steer_index = 0
        return True

    if Button.LEFT_PLUS in buttons:
        state.inc_speed()
        return True

    if Button.LEFT_MINUS in buttons:
        state.dec_speed()
        return True

    if Button.RIGHT_PLUS in buttons:
        state.inc_steer()
        return True

    if Button.RIGHT_MINUS in buttons:
        state.dec_steer()
        return True

    return False


def update_display(hub: InventorHub, state: State):
    """
    Updates the display on the hub based on the current state.
    """
    i = state.speed_index
    j = state.steer_index

    if i == 0 and j == 0:
        pulse = state.timer.time() // 10 % 200

        if pulse > 100:
            pulse = 200 - pulse

        half_pulse = pulse // 2

        hub.display.pixel(0, 2, 0)
        hub.display.pixel(1, 2, half_pulse)
        hub.display.pixel(3, 2, half_pulse)
        hub.display.pixel(4, 2, 0)

        hub.display.pixel(2, 2, pulse)

        hub.display.pixel(2, 0, 0)
        hub.display.pixel(2, 1, half_pulse)
        hub.display.pixel(2, 3, half_pulse)
        hub.display.pixel(2, 4, 0)
    else:
        # speed indication
        hub.display.pixel(0, 2, 100 if i > 3 else (50 if i > 2 else 0))
        hub.display.pixel(1, 2, 100 if i > 1 else (50 if i > 0 else 0))
        hub.display.pixel(3, 2, 100 if i < -1 else (50 if i < 0 else 0))
        hub.display.pixel(4, 2, 100 if i < -3 else (50 if i < -2 else 0))

        # center pixel
        hub.display.pixel(2, 2, 100)

        # steering indication
        hub.display.pixel(2, 0, 100 if j > 3 else (50 if j > 2 else 0))
        hub.display.pixel(2, 1, 100 if j > 1 else (50 if j > 0 else 0))
        hub.display.pixel(2, 3, 100 if j < -1 else (50 if j < 0 else 0))
        hub.display.pixel(2, 4, 100 if j < -3 else (50 if j < -2 else 0))


def idle_gen():
    """
    Yields forever (doesn't do anything).
    """
    while True:
        yield


def get_action(gelo: Gelo, state: State):
    """
    Gets an action based on the current state.
    """
    if state.speed_index == 0:
        return idle_gen()

    return gelo.walk_gen(state.speed(), state.steer())


#######################################################
# Main program
#######################################################


with Gelo() as gelo:
    # yellow indicates we are waiting for remote
    gelo.hub.light.on(Color.YELLOW)

    remote = Remote()

    # green indicates that remote is connected
    gelo.hub.light.on(Color.GREEN)

    # inital state
    state = State()
    action_iter = idle_gen()
    pressed_iter = pressed_oneshot_gen(remote)

    while True:
        # when a button is pressed, select a new action
        if handle_pressed(next(pressed_iter), state):
            action_iter = get_action(gelo, state)

        # update the outputs based on the current state
        update_display(gelo.hub, state)
        next(action_iter)

        wait(10)
