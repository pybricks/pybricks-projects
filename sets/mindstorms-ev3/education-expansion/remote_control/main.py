from pybricks.hubs import EV3Brick
from pybricks.parameters import Color, Port, Stop, Direction
from pybricks.ev3devices import Motor
from pybricks.tools import wait, StopWatch, run_task
from pybricks.messaging import RFCOMMSocket
from micropython import const
from umath import sin, pi
import ustruct

hub = EV3Brick()

# The large wheel connected to port A is the steering wheel.
axis1_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)

# The small wheel connected to port D is the throttle trigger.
axis2_motor = Motor(Port.D)

# These variables are used to compute a duty cycle that resists the user's
# attempt to turn the motor in a direction with a low duty cycle, while still
# allowing us to tell when the user stops turning the motor in that direction.

OSCILLATE_PERIOD = const(22)  # ms
ANGULAR_FREQ_COEFF = 2 * pi / OSCILLATE_PERIOD

def resist_duty(base_duty, t, static_friction_duty) -> int:
    """Computes a duty cycle that oscillates around a base duty cycle."""
    added_duty = sin(t * ANGULAR_FREQ_COEFF) * static_friction_duty
    return int(base_duty + added_duty)

# The fraction of the motor's power that is required to overcome the
# motor's static friction. For large motors, it's a greater fraction
# of the motor's maximum power than for small motors.
LARGE_MOTOR_STATIC_FRICTION_DUTY = const(20)
SMALL_MOTOR_STATIC_FRICTION_DUTY = const(10)

# The bluetooth address of the remotely controlled device. Change this
# to the address printed by your remote controlled device program.
TARGET_BLUETOOTH_ADDRESS = 'F0:45:DA:13:1C:8A'

def steering_wheel(t: int) -> int:
    """Drives the steering wheel process.

    1. Provides force-feedback for the steering wheel depending on how
       far it is from neutral.
    2. Returns an integer between -127 and 127 that expresses how far
       the steering wheel is from neutral.

    Args:
        t (int): The time in milliseconds since the process started.
    Returns:
        int: An integer between -127 and 127 representing the steering
                wheel position.
    """
    STEERING_RESIST_MAX_DUTY = const(30)
    STEERING_DEAD_ZONE = const(10)  # degrees
    RESIST_START_ANGLE = const(50)  # degrees - angle where resistance begins
    RESIST_RANGE = const(130)  # degrees - range over which resistance ramps to max
    MAX_ANGLE = const(180)  # degrees - maximum steering wheel angle

    angle = axis1_motor.angle()
    speed = axis1_motor.speed()
    abs_angle = abs(angle)

    if abs_angle < STEERING_DEAD_ZONE:
        hub.light.on(Color.BLUE)
        axis1_motor.brake()
        if abs_angle < 1:
            axis1_motor.stop()
    elif (angle > 0) != (speed > 0) and speed != 0:
        # If the motor is currently turned in one direction and turning back
        # toward zero, encourage that motion by running the motor toward zero.
        axis1_motor.dc(-30 if angle > 0 else 30)
    else:
        # If the user is currently turning the motor away from zero, resist
        # that movement with a duty cycle that increases the further we get
        # from zero. Duty cycle of resistance maxes out at 15%.
        base_duty = STEERING_RESIST_MAX_DUTY * max(0, min(1, (abs_angle - RESIST_START_ANGLE) / RESIST_RANGE))
        duty = resist_duty(base_duty, t, LARGE_MOTOR_STATIC_FRICTION_DUTY)
        duty = duty if angle < 0 else -duty
        axis1_motor.dc(duty)
    
    # Scale the return value: 0 in dead zone, ±127 at max resistance angle
    if abs_angle < STEERING_DEAD_ZONE:
        return 0
    
    scaled = int(127 * (abs_angle - STEERING_DEAD_ZONE) / (MAX_ANGLE - STEERING_DEAD_ZONE))
    scaled = min(127, scaled)  # Cap at 127
    return scaled if angle > 0 else -scaled


AXIS2_MAX_THROW = const(29)  # degrees - maximum throw for throttle


def throttle(t: int) -> int:
    """Returns an integer between 0 and 127 representing the throttle position."""
    angle = axis2_motor.angle()
    
    # This extra duty we apply helps keep the motor unstuck, which makes
    # it easier for the user to adjust it with small increments.
    axis2_motor.dc(resist_duty(0, t, SMALL_MOTOR_STATIC_FRICTION_DUTY))
    
    scaled = int(127 * angle / AXIS2_MAX_THROW)
    return min(127, max(0, scaled))


# How often we send update messages to the remote controlled device.
UPDATE_PERIOD = const(16)  # ms

async def main():
    """Main remote control process."""
    with RFCOMMSocket() as sock:
        while True:
            hub.light.on(Color.RED)
            await sock.connect(TARGET_BLUETOOTH_ADDRESS)
            hub.light.on(Color.GREEN)
            stopwatch = StopWatch()
            update = StopWatch()
            
            while True:
                t = stopwatch.time()
                wheel = steering_wheel(t)
                throttle_value = throttle(t)
                
                if update.time() < UPDATE_PERIOD:
                    # We drive the steering wheel and throttle at a
                    # higher rate than we send out updates, because
                    # their motors need to be adjusted more frequently
                    # than our RC device needs to receive updates.
                    await wait(1)
                    continue
                    
                await sock.write(ustruct.pack('>bb', wheel, throttle_value))
                update.reset()
                
                print(f"AXIS1:{wheel} AXIS2:{throttle_value}")
                await wait(1)

run_task(main())