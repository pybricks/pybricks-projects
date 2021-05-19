---
title: "Obstacle Avoidance"
maintainer:
    user: "pybricks"
    name: "The Pybricks Team"
image:
    local: "obstacle-avoidance.jpg"
description:
    "Make the truck drive around autonomously using sensors."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.core.pdf/6314518.pdf
---

# Selecting a sensor
This project will work with any sensor that can measure distance.

You can use
the [Color and Distance sensor](https://docs.pybricks.com/en/latest/pupdevices/colordistancesensor.html)
as in this example, but you can also use the
[Ultrasonic Sensor](https://docs.pybricks.com/en/latest/pupdevices/ultrasonicsensor.html)
or the
[Infrared Sensor](https://docs.pybricks.com/en/latest/pupdevices/infraredsensor.html).
Mount the sensor somewhere on the front of your truck.

# Main program

This program builds on the basic [driving example](../driving). It makes the
truck back up and turn when it detects an obstacle.

{% include copy-code.html %}
```python
{% include_relative main.py %}
```

