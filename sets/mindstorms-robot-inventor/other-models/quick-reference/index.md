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

You can use the code for this project as a quick reference to the various functions
available for the hub, motors, and sensors that come in the 51515 kit. The program
includes most (but not all) of the functions available for these devices.

You can actually run the entire program on an Inventor hub with 3 motors on ports 
A, B, and E, color sensor on C, and distance sensor on D, but the real purpose is 
to show function syntax examples in the code. 

### Notes for Beginners

If you are new to Python programming note that most of the Pybricks functions require
numbers or other information as input. For example:
```python
    arm.run_angle(500, 180)     # rotate at speed 500 for 180 degrees
```
Many of the examples in the reference use variables (named values) to make them easier 
to read, so instead will be written like this:
```python
    speed = 500     # (deg/s)
    angle = 180     # (deg)
    arm.run_angle(speed, angle)     # rotate by angle
```
In all Python code, text after a # character is a "comment" (a note for human readers, 
not part of the code), so here you will find info like units and other hints.

At the end of the program there is also a quick reference for basic Python syntax.

## Program

{% include copy-code.html %}
```python
{% include_relative Quick_Ref.py %}
```
