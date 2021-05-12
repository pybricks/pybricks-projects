---
title: "Steer Bot"
maintainer:
    user: "GusJansson"
    name: "Gus Jansson"
image:
    local: "steerbot.jpg"
video:
    youtube: "i4WPa-rtFB8"
description:
    "Super fast line following robot with Ackermann steering."
building_instructions:
    local: "steerbot-instructions.pdf"
---

## Description

A robot with car like steering has been one of my favorite exercises in robot
building. This project, in fact, is largely a variation of what I have
previously done with the LEGO RCX, the NXT and to a lesser extent the EV3. But
with the 51515 set I as able to take advantage of improved resolution of the
color sensor as well as some cool features of Pybricks to make the main
tracking code pretty simple.

The robot features Ackermann steering. This means that the steering linkage is
more trapezoidal than parallel. The front wheels are only parallel when the
steering is pointing straight ahead. When it turns the inside wheel turns
sharper than the outside wheel so the wheels track more accurately since the
inside wheel has a tighter turning radius. This is particularly important in
order to achieve tight overall turning radius with a relatively wide robot.

The robot uses the Color Sensor mounted on an axle high and attached to the
steering motor. This means that in order to track a line, actually just the
edge of the line, the tracking code tries to keep the sensor on the edge of
the line. If the sensor is on the edge, then as the robot drives it will follow
the edge since the robot is now steering to where the edge is in front of the
robot. The sensor is mounted high in order to give a gradual reading over the
edge so that while near the edge the program can determine where the edge is
relative to the sensor.

The driving is done through the super cool 5 gear differential that is included
with the set. This is the first time I use this LEGO differential and I love
it! The drive motor is actually gearing up with the intention of being able to
go really fast. On my tight test track I was never able to make it go full
speed without running off the line.

## Program


{% include copy-code.html %}
```python
{% include_relative main.py %}
```
