---
title: "Wack3m"
maintainer:
    user: "TheVinhLuong102"
    name: "The Lương-Phạm Family"
image:
    local: "wack3m.jpg"
    credit: "LEGO"
video:
    youtube: "ksojLbHrhJ8"
description:
    "Designed by [Martyn Boogaarts](https://www.robotmak3rs.com/Martyn-Boogarts). This is an arcade-style game that tests your reaction speed. The robot pops up disks that you have to whack as quickly as possible using the wack-wheel hammer. Challenge your friends and see who wackedy-wacks the fastest!"
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.extra.pdf/31313_X_WACK3M.pdf
---


This program requires [LEGO® MINDSTORMS® EV3 MicroPython v2.0](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3) installed on the EV3 Hub.

How to play: Press the Touch Sensor to start a game. Each game has ten rounds of whacking, and your average response time is measured.

The code for the `Wack3m` class is in `wack3m.py` as follows:

{% include copy-code.html %}
```python
{% include_relative wack3m.py %}
```

The code for the main program is in `main.py` as follows:

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
