#!/usr/bin/env pybricks-micropython


from el3ctric_guitar import El3ctricGuitar


guitar = El3ctricGuitar()

guitar.start_up()

while True:
    guitar.play_note()
