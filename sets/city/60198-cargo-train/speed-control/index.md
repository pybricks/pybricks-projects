---
title: "Train speed control"
maintainer:
    user: "pybricks"
    name: "The Pybricks Team"
image:
    local: "train-load.jpg"
video:
    youtube: "Qc7sIkzEgIc"
description:
    "Make a train drive at a constant speed, independent of load and battery
    level."
building_instructions:
    external:
    - https://www.lego.com/cdn/product-assets/product.bi.core.pdf/6245902.pdf
    - https://www.lego.com/cdn/product-assets/product.bi.core.pdf/6245905.pdf
    - https://www.lego.com/cdn/product-assets/product.bi.core.pdf/6245917.pdf
    - https://www.lego.com/cdn/product-assets/product.bi.core.pdf/6245924.pdf
    - https://www.lego.com/cdn/product-assets/product.bi.core.pdf/6245926.pdf
    - https://www.lego.com/cdn/product-assets/product.bi.core.pdf/6245931.pdf
code: "#program"

---

## Design modifications
Build any train using the standard instructions. Mount the
[color distance sensor][colordistancesensor] in the frame, as shown in the
video. Connect the motor to port A and connect the sensor to port B.

## Program

This program makes the train drive at a constant speed. It works by counting
the tracks using the Color and Distance Sensor. The motor "power" is
automatically increased if the counted position is below the target position,
and reduced if it is too far ahead. The target position steadily increases
over time. This makes the train follow the target at the same speed.

In this video, there's a white surface underneath the tracks. If your
background is different, you can change the reflection values
accordingly, as shown in the comments below. You could also adapt the script
so it responds to different colors instead of reflected light intensity.

{% include copy-code.html %}
```python
{% include_relative main.py %}
```

[colordistancesensor]: https://docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html

