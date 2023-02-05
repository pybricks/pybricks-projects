---
title: "Fast Block Flipper"
maintainer:
    user: "davecparker"
    name: "Dave Parker"
image:
    local: "block-flipper.JPG"
video:
    youtube: "IBtZhiKN9qI"
description:
    "A Four-motor robot that quickly moves and flips blocks"
building_instructions:
    external: https://www.onekitprojects.com/51515/4-motor-arm
code: "#program"
---

## Description

This robot arm has four motors to allow it to grab, lift, flip, and move blocks
between the three small raised platforms. The program uses some of the advanced
motor control APIs to control all four motors at the same time and get fast
and accurate motion. 

## Instructions

This program controls the 4-Motor Arm autonomously, so you don't have to build
the hand controller. You can just attach the hub to the base as shown.

Start with the two blocks on the outside (left and right) platforms, and the arm
near the middle between them. 

## Program

{% include copy-code.html %}
```python
{% include_relative block-flipper.py %}
```
