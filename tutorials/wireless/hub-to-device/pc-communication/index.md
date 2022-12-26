---
title: "Hub to PC Communication"
maintainer:
    user: "pybricks"
    name: "The Pybricks Team"
image:
    local: "hub-to-pc.png"
description:
    "This project shows how you can exchange data between the hub and a script 
    running on your computer."
---

# Standard input and output

When you run a program, input and output is normally handled via the Pybricks
Code terminal pane, as demonstrated [here](../pc-keyboard/).

But once disconnected from Pybricks Code, you can use other devices and
programs to connect to the hub. In this project, you'll learn how to connect
your computer to the hub and send data to it using a Python script.

**Pybricks BLE characteristics**

The Pybricks firmware supports three Bluetooth Low Energy (BLE)
[characteristics](https://github.com/pybricks/technical-info/blob/master/pybricks-ble-profile.md):

1. Pybricks Command/Event Characteristic
2. Pybricks Hub Capabilities Characteristic
3. Nordic UART Service

The first two are specific to Pybricks. They are used to download programs to
the hub and run them.

The Nordic UART Service (NUS) is a standard
characteristic that can be thought of as a BLE serial port. The Pybricks
firmware uses it for things like ``input()`` and ``print()``.

**Characteristics, simplified**

Fortunately, you don't need to know about the two Pybricks characteristics if
you use Pybricks Code to download a program to the hub in advance. Then the
script on your computer only has to deal with the Nordic UART Service. This
works as follows:

1. Create a Pybricks program that handles input and output as you like. 
   We'll show you an example below.
2. Disconnect from Pybricks Code.
3. Write a script to find the hub and connect to it. We'll show you an example
   for this too.
4. Start your (previously loaded) Pybricks script with the button.
5. Exchange data with the hub.

The next sections take you through this step by step.

# Handling input and output on the hub

From the hub's point of view, all input and output happens via the
``usys.stdin`` and ``usys.stdout`` files, whether you use Pybricks Code or any
other tool.

In this example, we'll make the hub listen for incoming data via ``stdin`` and
use it to control the direction of a motor:

- If the hub receives ``fwd``, the motor goes forward.
- If the hub receives ``rev``, the motor goes in reverse.
- If the hub receives ``bye``, the hub ends the program.
- If the hub receives something else, the motor stops.

For each successful motor command, the hub will respond with ``OK`` via
``stdout``. In this example, ``print("OK")`` would have achieved the same
result, but ``print`` limits you to standard characters only.

To try it out, run the following program on the hub and type ``fwd`` or ``rev``
in the terminal pane. You should see the motor respond accordingly, and get
``OK`` in response.

Now end the program by pressing the button or by typing ``bye``.

{% include copy-code.html %}
```python
{% include_relative main.py %}
```

This program works on all hubs except for the BOOST Move Hub, since it does not
support the ``usys`` or ``uselect`` module. You can still make it work on that
hub by using the ``input()`` and ``print()`` functions instead.

# Sending and receiving data from a PC

The next step is to get your computer ready to connect to the hub and exchange
some data. In essence, your script will play the role that the Pybricks Code
terminal pane normally would.

To accomplish this, we need to:
- Scan for the hub.
- Connect to the hub.
- Get the NUS characteristic.
- Read and write data.

Since this is not specific to Pybricks, you can use any programming language or
device that supports the Nordic UART Service. You could even do this from
another MicroPython board.

In this example, we'll show you how
to do it with Python and a BLE library called ``bleak``:

```
pip install bleak
```

The asynchronous ``main()`` function in the example below will scan for the hub
and connect to it. Note that it can only find the hub if no other apps (like
Pybricks Code) are connected, and if no program is currently running.

Once it finds the hub and establishes the connection, you can start the
previously loaded program on the hub by pressing the button.

At this point, the script sends several ``fwd`` and ``rev`` commands. The hub
should respond by making the motor turn and by returning ``OK``. After doing
this five times, sending ``bye`` causes the program on the hub to terminate.

{% include copy-code.html %}
```python
{% include_relative demo.py %}
```

When you run the program, the expected output should be similar to:

```
python ./demo.py 
Start the pre-load program on the hub now with the button.
Received: bytearray(b'OK')
Received: bytearray(b'OK')
Received: bytearray(b'OK')
Received: bytearray(b'OK')
Received: bytearray(b'OK')
Received: bytearray(b'OK')
Received: bytearray(b'OK')
Received: bytearray(b'OK')
Received: bytearray(b'OK')
Received: bytearray(b'OK')
Hub was disconnected.
```


# Further exploration: BLE terminal

In the aforementioned examples, you prepared the hub to handle commands with a
specific set of actions and response messages. Using a small set of messages
and commands is usually the quickest and most reliable way to do it.

If you want to make it more generic, it is also possible to programatically
interact with the REPL so you can access the entire Pybricks API remotely.
The REPL is normally activated with the REPL button in Pybricks
Code, but you can also enter it from a program on the hub as follows:

{% include copy-code.html %}
```python
raise KeyboardInterrupt
```

On the computer, you can run a script [like this](https://github.com/hbldh/bleak/blob/master/examples/uart_service.py) to emulate a UART terminal. You may need to modify the scanning
filters to connect to the hub.

# Further exploration: Automatic start

So far, we had to load a script on the hub in advance to avoid dealing with the
two Pybricks BLE characteristics. 

If you want to automate the process of loading the script as well, you can
use the [pybricksdev](https://github.com/pybricks/pybricksdev/) library, which
implements both Pybricks characteristics.
