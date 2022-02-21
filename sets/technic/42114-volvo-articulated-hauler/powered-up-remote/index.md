---
title: "Powered Up Remote Control"
maintainer:
    user: "repkovsky"
    name: "Repkovsky"
image:
    local: "42114_88010.jpg"
    credit: "LEGO"
description:
    "Control the Volvo articulated hauler with the Powered Up Remote!"
video:
    youtube: "j4ZxOhXygNY"
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.core.pdf/6396116.pdf
code: "#program"
---


# Manual and automatic switching mode

The program for controlling Technic Volvo Articulated Hauler with remote
control is a bit more complicated than the other remote control programs
because of the 3-gear gearbox, which works both in manual and automatic mode.

Manual gear switching requires not only detection whether the remote button is
pressed or not, but also detection of the button press (or release) moment
itself. This is realized using the ``Key`` class.

The automatic gearbox needs to detect the proper time for switching the gear
up or down. This is possible by measuring the speed of XL motor, when it is
running. If the speed is systematically very low, the gear is decreased.
If the speed is systematically close to maximum, the gear is increased.

To make speed measurement robust to random variations, values obtained from
the speed sensor are filtered using simple
[exponential smoothing](https://en.wikipedia.org/wiki/Exponential_smoothing).
Threshold values of speed, measurement time and smoothing constant are defined
by the constants `HI_SPEED, LO_SPEED`, `STABLE_SPEED_TIME` and `SMOOTHING`.
If the automatic gearbox does not change gears even if Hauler reaches full
speed, `HI_SPEED` should be decreased. Speed tracking, keeping the current
state of gearbox and handling the remote/hub LEDs was implemented in the
``Gearbox`` class.

# Driving and switching gears

By default, the left controller controls the left/right steering, and the right
controller determines the direction of driving. This can be changed easily by
setting the constant `LEFT_STEER_RIGHT_DRIVE` to False.

The gearbox can be used in two modes, as in the original LEGO smartphone app:
*automatic* and *manual*. You can switch between the modes by pushing the green
button on the remote. *Automatic* is default starting mode, but this can be
easily changed by modifying constant `INIT_GEARBOX_AUTO`.

In the *automatic* mode, gears are changed when program detects that motor's
speed is too slow or close to maximum speed. The current gear is indicated by
the color of the remote's LED:
1. Cyan
2. Blue
3. magenta
    
To enable dumper (remote LED: green), press the right red button on the remote.
To go back to driving mode, press left red button. If drive is idle for time
longer than defined in constant `GEAR_RESET_TIMEOUT`, the gear is set to 1.

In the *manual* mode, the gear is decreased by pressing left red button, and
increased with right red button. Gearbox positions are indicated by the color
of LED:

1. Yellow
2. Orange
3. Red

Sometimes gearbox tends to jam. If the target angle of gear selector is not
reached within the time defined by `GEAR_SWITCH_TIMEOUT` (1.5 sec by default),
the automatic gearbox reset is performed. The hub LED changes to red, while
the gearbox is recalibrated, which sets the gear to 1.

![](./remote_description.png)

# Program

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
