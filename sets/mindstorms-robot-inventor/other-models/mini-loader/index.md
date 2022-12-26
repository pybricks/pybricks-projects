---
title: "Remote-controlled Mini Loader"
maintainer:
    user: "davecparker"
    name: "Dave Parker"
image:
    local: "mini-loader.JPG"
video:
    youtube: "L0gnDPXkx4U"
description:
    "Mini Loader controlled with LEGO Bluetooth Remote"
building_instructions:
    external: https://www.onekitprojects.com/51515/mini-loader
code: "#program"
---

## Description

This Mini Loader has four motors to allow it to drive, steer, lift, and dump.
The program connects to the LEGO Bluetooth Remote and uses the remote's buttons 
in several ways to implement a variety of control features. 

## Instructions

Twist the controls on the remote to make the left side vertical with + on top,
and the right side horizontal with + on the right.

Establish the connection between the hub and remote using these steps:
1. Download the Pybricks program to the hub.
2. If the program is running (display animating), press the hub button to stop it. 
3. Press the green center button on the Remote (light flashes white).
4. Immediately press the Inventor hub button to run the program.
5. If the connection is successful, both the remote and hub lights turn green. 

The remote has two modes, which you toggle between using the green center button 
on the remote. The modes are indicated by both the remote and hub lights. 
Use Drive mode (green) to drive and steer, and Lift mode (Orange) to control the lift. 

### Drive Mode (Green light)

Use the left side buttons to control the drive direction and the right side buttons 
to steer. You can drive and steer at the same time, or just steer to pivot in place.

By holding down either of the two red buttons, you can reduce both the driving and steering
speed for more precise positioning. You can do this either by holding a red button 
with one thumb (like a shift key) while using +/- controls with your other thumb,
or with a single thumb, you can roll between pressing both Center and +/- at the same time
(slow) or just +/- (fast). 

### Lift Mode (Orange Light)

Tap the three left side buttons to make the lift and scoop move together to three 
preset positions: Carrying High, Carrying Middle, or Ready Low.

Tap -/+ on the right side to dump/undump the scoop without moving the lift. 

The red right center button runs a special feature to help position
the mini loader to prepare to dump. Pressing and holding this button will make
the robot drive straight forward until the distance sensor measures 5 cm
(or until you release the button to cancel). The lights on the ultrasonic sensor
are turned on when the robot is using them, so a fun side effect is that quickly
tapping the right center button just flashes the sensor lights.

## Program

{% include copy-code.html %}
```python
{% include_relative miniLoader_RC.py %}
```
