---
title: "Powered Up Remote Control"
maintainer:
    user: "JorgePe"
    name: "Jorge Pereira"
image:
    local: "powered-up-remote-buggy.jpg"
description:
    "Control the Technic Off-Road Buggy with the Powered Up Remote."
video:
    youtube: 6Urq0aX2jR4
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.core.pdf/6351188.pdf
code: "#program"
---

In this project we'll show you how to control the Technic Off-Road buggy with
the Powered Up remote.

# Program

This program is similar to most driving vehicles in the Technic series. Check
out the [Technic X-treme Off-Roader](../../42099-off-roader) examples for
additional tips and tricks.

When the program starts, it connects to your remote and the steering mechanism
is calibrated. Then you are ready to drive.

The left channel controls the steering and right channel drives the car.

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
