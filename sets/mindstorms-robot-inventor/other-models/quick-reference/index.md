---
title: "Quick Reference for Robot Inventor"
maintainer:
    user: "davecparker"
    name: "Dave Parker"
image:
    local: "Quick_Ref.JPG"
description:
    "Quick Reference examples for the Robot Inventor hub, motors, and sensors"
code: "#program"
---

## Description

You can use the code for this project as a quick reference to the various Pybricks
functions available for the hub, motors, and sensors that come in the 51515 kit. 
The program includes most (but not all) of the functions available for these devices.

You can actually run the entire program on an Inventor hub with 3 motors on ports 
A, B, and E, color sensor on C, and distance sensor on D, but the real purpose is 
to show function syntax examples in the code. 

### Understanding the Python Syntax

If you are new to Python programming, note that most of the Pybricks commands will
fit on one line and consist of three parts, for example:
```python
    arm.run_angle(500, 180)     # rotate at speed 500 for 180 degrees
```
1. Here ``arm`` is the name of the *object*, which is the motor, sensor, or device
that the command refers to. These names are defined at the top of the program
in the Getting Started section.
2. ``run_angle`` is the *function* name. Pybricks defines these, and this Quick 
Reference will help you discover and learn them.
3. The numbers ``(500, 180)`` are the *input parameters*, which give the function
additional information it needs to do the desired action.

Any text after the ``#`` symbol is a *comment*, which is just a note for human readers 
(ignored by the computer) to make the code easier to understand.

To make the input parameters easier to understand, many of the examples in the program
use *variables* (names) for them like this: 
```python
    speed = 500     # (deg/s)
    angle = 180     # (deg)

    arm.run_angle(speed, angle)     # rotate by angle
```
For other parts of general Python syntax, the program has a quick guide at the end
for the most common structures.

## Program

{% include copy-code.html %}
```python
{% include_relative Quick_Ref.py %}
```
