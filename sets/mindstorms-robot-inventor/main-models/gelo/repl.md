---
title: Command prompt
description: Control Gelo with the interactive command prompt
maintainer:
    user: "pybricks"
    name: "The Pybricks Team"
image:
    local: ../gelo.jpg
    credit: LEGO
building_instructions:
    external: https://www.lego.com/cdn/product-assets/product.bi.additional.main.pdf/51515_Gelo.pdf
code: "#program"
---

## Using the command prompt

Python has an interactive command prompt. This is also sometimes called the
REPL (Read Evaluate Print Loop). It can be used to run Python code as you
type it in.

Save the program below as `gelo_repl.py` in Pybricks Code. And make sure you
have the [gelo.py](../#main-program) saved there too.

Then connect to Gelo and run the program. In the terminal window in Pybricks
Code, you will see a prompt like this:

```
>>>
```

Type in a command like this and press enter:

```
>>> gelo.walk()
```

### Tips

* To save some typing, after typing `gelo.`, you can press the <kbd>tab</kbd>
  key to provide a list of available methods. Then type the first few letters
  and press <kbd>tab</kbd> again to complete the name.
* To cancel a running command, you can press <kbd>ctrl</kbd>+<kbd>c</kbd>.


## Program

{% include copy-code.html %}
```python
{% include_relative gelo_repl.py %}
```
