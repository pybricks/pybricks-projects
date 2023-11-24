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

**Channels**

In Pybricks, all broadcasting data is assigned a *channel*. This helps you tell
data apart when multiple hubs are broadcasting at the same time. For example,
one hub might be broadcasting tilt sensor data on channel 1 while another hub
broadcasts measurements on channel 2.

To prepare the hub to send and receive data with these channels, you initialize
the hub class as follows:

```python
# Prepare the hub for sending.
hub = ThisHub(broadcast_channel=1)
```

```python
# Prepare the hub for receiving.
hub = ThisHub(observe_channels=[1, 2])
```

**Sending and receiving data**

You can send data like this:

```python
# Get a tuple of pitch and roll angles.
data = sensor.tilt()

# Send it out to anyone listening.
hub.ble.broadcast(data)
```

On another hub, you can receive it as follows:

```python
# Try to read previously received tilt data.
data = hub.ble.observe(1)

# Check if there was any data yet:
if data is not None:
    # There was, so let's print it.
    pitch, roll = data
    print(pitch, roll)
```

When sending data, your values will be automatically encoded into a format
suitable for broadcasting. You can send integers (`1`, `-5`, ...), floats
(`1.0` `-5.3`, ...), booleans (`True`, `False`), strings (`"example"`), bytes
(`b"\x00\x02"`) or tuples thereof.


# Running the example programs

The following examples shows the broadcasting feature in action to provide
wireless bidirectional communication.

One hub sends tilt sensor data to control a driving vehicle. The vehicle
sends back a distance measurement to show a warning light for nearby obstacles:

**Run this program on the sender**

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

# Known issue: Slow communication while connected to computer

If the hub is still connected to the computer, the bluetooth chip is quite busy
and data broadcasting may be slow. Especially on the Technic Hub and the City
Hub. On the Move Hub, it cannot broadcast at all while connected to the PC.

To work around it, just load the program onto the hub and disconnect from your
computer. You can just restart the program with the hub button.
