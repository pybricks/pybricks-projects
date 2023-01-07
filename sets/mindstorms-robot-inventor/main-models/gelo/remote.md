---
title: "Remote control Gelo"
maintainer:
    user: "pybricks"
    name: "The Pybricks Team"
image:
    local: "../gelo.jpg"
    credit: "LEGO"
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.main.pdf/51515_Gelo.pdf
code: "#program"
---

## Instructions

This program requires the LEGO Powered Up remote control. The left <kbd>+</kbd>
and <kbd>-</kbd> buttons control the speed and the right <kbd>+</kbd> and
<kbd>-</kbd> buttons control the steering. Either red button will make Gelo stop.

![image of LEGO remote](../remote.png)

This script makes use of the [gelo.py](../#gelo-module) module, so make
sure to save that program in Pybricks Code first.

Then save the script below as `gelo_remote.py` and run it.

When the program starts, the light will turn yellow. This means Gelo is waiting
to connect to the remote control. Turn on the remote and it will connect
automatically and the light on Gelo will turn green. Then you can press the
buttons on the remote to control Gelo.

## Program

{% include copy-code.html %}
```python
{% include_relative gelo_remote.py %}
```
