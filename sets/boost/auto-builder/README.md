---
permalink: /projects/sets/boost/auto-builder/
title: "LEGO Boost Auto Builder"
maintainer:
    user: "pybricks"
    name: "The Pybricks Authors"
image:
    local: "photo.jpg"
    credit: "LEGO"
video:
    youtube: "https://www.youtube.com/embed/TXvCEK1MNGQ"
description:
    "The Auto Builder builds LEGO figures autonomously. These Python scripts
    make it work smoothly and accurately."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.main.pdf/17101_A_AutoBuilder.pdf
---

# Coding instructions

This program resets the motors to known positions, and then constructs the
LEGO figure brick-by-brick.

This works by repeatedly:
- moving the belt motor to the given brick;
- picking the brick up by moving the arm down and up;
- moving the belt back to the base position;
- putting the brick down.

The brick positions are given as the degrees the belt motor turns relative to
the base position. You can tweak these values by a few degrees if needed.

```python
{% include_relative main.py %}
```


# Further exploration

The provided program is very basic, demonstrating only the core principles.
Here's a few ideas and challenges for further exploration:
- Change the order of the bricks in the `for`-loop to build something else.
- Instead of pushing the element down for two seconds, you could stop sooner.
  Try experimenting with the [`run_until_stalled`](https://docs.pybricks.com/en/latest/pupdevices/motor.html#pybricks.pupdevices.Motor.run_until_stalled)
  method. This can speed up the build process.
- Speaking of increasing speed, how fast can you make it? Optimize this robot
  and set a new world record!
