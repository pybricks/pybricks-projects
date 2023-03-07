---
title: "Communicating with hubs that run official LEGO firmware"
maintainer:
    user: "pybricks"
    name: "The Pybricks Authors"
image:
    local: "duplo-spike-small.jpg"
description:
    "This project shows how you can control the Duplo Hub
    (or any hub running the official firmware), from a hub that runs Pybricks."
building_instructions:
    local: instructions.pdf
video:
    youtube: "DpQg4trW1y0"
code: "#the-duplo-train-class"
---

# LEGO Wireless Protocol 3.0 (LWP3)

Out of the box, most LEGO hubs support the [LEGO Wireless Protocol 3.0](https://lego.github.io/lego-ble-wireless-protocol-docs/) (LWP3). Pybricks has a
builtin [`LWP3Device`](https://docs.pybricks.com/en/latest/iodevices/lwp3device.html)
class that lets a hub running Pybricks connect to another hub that runs the
standard firmware.

This is particularly useful if you want to control a hub that is not directly
supported by Pybricks, or if you don't want to install Pybricks on all of
your hubs.

In this example, we'll show you how it works for the Duplo Hub. You can adapt
the example to send and receive other commands or control other hubs, by
following the LWP3 documentation.

# The Duplo train class

The code for this example is split into two parts. First, create a new file
called `duplo.py` with the following contents.

It provides a class for connecting to the Duplo Hub and sending commands to it.

{% include copy-code.html %}
```python
{% include_relative duplo.py %}
```

# The main program

Next, create another program called `train_driver.py` with the following
contents.

This program imports the `DuploTrain` class we just made to interface with the
Duplo Hub in a simple way. Instantiating the `train` object will set up the
connection.

You can use the `choo_choo` method to make a sound, the `light`
method to set the train front light color, and the `drive` method to drive at
a selected speed (-100 to 100).

To try this project, run this program and turn on the train. The train should
make a connection sound and you're ready to go.

{% include copy-code.html %}
```python
{% include_relative train_driver.py %}
```

