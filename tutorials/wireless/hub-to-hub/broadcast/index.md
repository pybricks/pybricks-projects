---
title: "Hub to hub communication using data broadcasting"
maintainer:
    user: "pybricks"
    name: "Pybricks and Nard Strijbosch"
image:
    local: "../hub-to-hub.png"
description:
    "This project shows how you can exchange data between two Pybricks hubs."
video:
    youtube: "i--8nBvNn_4"
---

# Experimental features ahead!

Hub to hub communication is still a work in progress. This page explains how
you can install an experimental release on the hub to try it out. This
functionality may change in the future and some things may not work.

# Data broadcasting

When a Bluetooth device is on but not yet connected to anything, it typically
broadcasts (_advertises_) some information about itself. This tells you what
it can do before you connect.

For example, Bluetooth earphones will advertise that they can play music, so
that your phone knows what to look for when it *scans* for speaker devices.

By constantly changing what information the hub advertises, we can broadcast
small amounts of information to nearby devices that are scanning for this
information.

This means that any number of nearby hubs can receive the broadcasted message
without having to set up a connection. This can be quite convenient, but you
can only broadcast small amounts of information at once, as explained below.

**Topics**

All broadcasting data is labeled with a _topic_. This helps you tell data
apart when multiple hubs are broadcasting at the same time. For example, one
hub might be broadcasting tilt sensor data with the topic ``"tilt"`` while
another hub broadcasts measurements with the topic ``"distance"``.

To prepare the hub to send and receive data with these topics, you initialize
the broadcast class as follows:

```python
# Import the experimental Broadcast feature.
from pybricks.experimental import Broadcast

# Prepare the hub for sending and/or receiving these topics.
radio = Broadcast(topics=["tilt", "distance"])
```

**Sending and receiving data tuples**

You can send data as a tuple of values:

```python
# Get some example data as a tuple.
example_data = (123, 456)

# Send it out to anyone listening.
radio.send("tilt", example_data)
```

On another hub, you can receive it as follows:

```python
# Try to read previously received tilt data.
data = radio.receive("tilt")

# Check if there was any data yet:
if data:
    # There was, so let's print it.
    pitch, roll = data
    print(pitch, roll)

```

When sending data tuples like these, your values will be automatically encoded
into a format suitable for broadcasting.

The following data tuples are allowed:

```python
# You can send up to 8 small values in the range +/- 32767.
# Each value counts as 2 bytes.
data = (-1, 2, 3000, 4, 5, 6, -32767, 32767)

# You can send up to 5 big values. Each value counts as 4 bytes.
data = (50000, -50000, 123456, 78910, 43210)

# You can send up to 5 floating point values. Each counts as 4 bytes.
data = (1.234, 3.1428)

# You can send up to 8 strings. Each character counts as 1 byte.
data = ("Hello", "World")

# You can combine up to eight of the above types.
# The total size must be 20 bytes or less.
data = (123, -50000, 3.1428, "Hi!")

```

**Sending and receiving raw data**

If you prefer to encode data yourself, you can send and receive bytes directly:

```python

# Send out up to 23 bytes to anyone listening.
radio.send_bytes("tilt", b"byte data!")

# Read up to 23 bytes.
data = radio.receive_bytes("tilt")
```

# Installing the experimental firmware

To use the broadcasting feature, you have to install a special version of the
Pybricks firmware that includes the ``Broadcast`` class:

1. Download the firmware file for your hub:
    - [Technic Hub](./technichub-firmware-build-2178.zip)
    - [City Hub](./cityhub-firmware-build-2178.zip)
    - [Essential Hub](./essentialhub-firmware-build-2178.zip)
    - [Inventor Hub and Prime Hub](./primehub-firmware-build-2178.zip)
2. In [Pybricks Beta](https://beta.pybricks.com/), open the settings menu.
3. Click ``Install Pybricks Firmware``.
4. Instead of selecting your hub, choose ``Advanced`` at the bottom.
5. Follow the instructions to select the firmware file you just downloaded.
6. The installation now proceeds as usual. Make sure to choose a descriptive
   hub name. This makes it easy to distinguish them later.
7. Start coding. You can open [Pybricks Beta](https://beta.pybricks.com/) in
   multiple different tabs. Use one tab for each hub.

# Running the example programs

The following examples shows the broadcasting feature in action to provide
wireless bidirectional communication.

One hub sends tilt sensor data to control a driving vehicle. The vehicle
sends back a distance measurement to show a warning light for nearby obstacles:

**Run this program on the remote**

You can use any hub with any type of sensor. For example, you could use the
built-in tilt sensor of the Technic Hub, Prime Hub, Essential Hub, or the
Inventor Hub. Alternatively, you could build your own remote control that uses
motors as input dials.

If you don't have the Color Light Matrix, you can delete the lines that
reference it, or adjust it to control the built-in hub light.

{% include copy-code.html %}
```python
{% include_relative remote.py %}
```

**Run this program on the vehicle**

You can use any hub with any type of motors. If you don't have a distance
sensor, you can delete the lines that make use of the Ultrasonic Sensor.

{% include copy-code.html %}
```python
{% include_relative vehicle.py %}
```

# Known issues: Slow communication while connected to computer

If the hub is still connected to the computer, the bluetooth chip is quite busy
and data broadcasting may be slow. Especially on the Technic Hub and the City
Hub.

This is something we are still working on. To work around it, just load the
program onto the hub and disconnect from your computer. You can just restart
the program with the hub button.

