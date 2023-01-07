---
title: Obstacle avoidance with Gelo
description: Gelo can autonomously roam around and avoid obstacles by using the ultrasonic sensor.
maintainer:
    user: "pybricks"
    name: "The Pybricks Team"
image:
    local: ../gelo.jpg
    credit: LEGO
code: "#program"
---

## Quick start

This script makes use of the [gelo.py](../#gelo-module) module, so make
sure to save that program in Pybricks Code first.

Then save the script below as `gelo_roam.py` and run it.

Gelo will walk forward until it "sees" an obstacle. Then it will randomly turn
left or right then start walking again until it sees the next obstacle.

## Program

{% include copy-code.html %}
```python
{% include_relative gelo_roam.py %}
```

## Change it up

Try changing the program to attack obstacles instead avoiding them.

* Change the main loop to turn until an obstacle is detected.
* Then walk towards the obstacle until Gelo crashes into it!
