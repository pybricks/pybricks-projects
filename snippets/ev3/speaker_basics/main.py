#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile


# Initialize the EV3
ev3 = EV3Brick()


# BEEP ########################################################################

# Simple beep
ev3.speaker.beep()

wait(1000)

# Interesting beeps
for f in range(100, 500, 100):
    ev3.speaker.beep(f)

wait(1000)


# PLAY NOTES ##################################################################

# Twinkle, Twinkle Little Star
A = ['C4/4', 'C4/4', 'G4/4', 'G4/4', 'A4/4', 'A4/4', 'G4/2',
     'F4/4', 'F4/4', 'E4/4', 'E4/4', 'D4/4', 'D4/4', 'C4/2']
B = ['G4/4', 'G4/4', 'F4/4', 'F4/4', 'E4/4', 'E4/4', 'D4/2'] * 2
TWINKLE = A + B + A

ev3.speaker.play_notes(TWINKLE)

wait(1000)


# PLAY FILE ###################################################################

ev3.speaker.play_file(SoundFile.HELLO)

wait(1000)


# TEXT TO SPEECH ##############################################################

# Say something in English
ev3.speaker.say('I am am E V 3. Pleased to meet you.')

# Say something in Danish + female
ev3.speaker.set_speech_options(voice='da+f5')
ev3.speaker.say('Leg godt!')

wait(1000)
