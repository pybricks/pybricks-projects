---
title: "Keyboard Remote Control"
maintainer:
    user: "pybricks"
    name: "The Pybricks Authors"
image:
    local: "keyboard-remote-truck.jpg"
description:
    "This project shows how you can control the truck with your keyboard."
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.core.pdf/6314518.pdf
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


# The remote control program

This program combines the keyboard example shown above with
the [basic driving program](../driving). This allows you to control the
truck using the numeric keys on your keyboard. If your keyboard does not have
separate numeric keys, just adapt the program to use other keys.

{% include copy-code.html %}
```python
{% include_relative main.py %}
```
