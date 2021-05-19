---
title: "Train slope detection"
maintainer:
    user: "pybricks"
    name: "The Pybricks Team"
image:
    local: "slope-detection.jpg"
video:
    youtube: "Wc0mRIBjhIU"
description:
    "Detect the slope of the track. This lets you determine where the train
     is on the circuit."
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
Build the train using the standard instructions. Mount the
[tilt sensor][tiltsensor]
horizontally in the train, with the cable side facing towards direction of
driving:

![](sensor-placement.jpg)

Connect the motor to port A and connect the tilt sensor to port B.

## Program

This program makes the train drive until it detects a slope of 8 degrees or
more. Then it drives back down.

{% include copy-code.html %}
```python
{% include_relative main.py %}
```

## Programming and running instructions
The train must start on a horizontal track. Then run the program.

[tiltsensor]: https://docs.pybricks.com/en/latest/pupdevices/tiltsensor.html

