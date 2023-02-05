---
title: "Control your hub with your keyboard"
maintainer:
    user: "pybricks"
    name: "The Pybricks Team"
image:
    local: "hub-keyboard.png"
description:
    "This project shows how you to use keyboard input in your programs."
---

# How it works

Your MicroPython programs can produce *output* using the `print` command, but
it can also read *input*. To enter input, just click on the terminal window
and press some keys.

![](./terminalwindow.png)

You can read keyboard presses using `stdin`, as shown in the example below.
Then you can make your program choose different behaviors based on which key
is pressed.

{% include copy-code.html %}
```python
{% include_relative remote.py %}
```
