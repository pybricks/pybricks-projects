#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Color
from pybricks.tools import DataLog

# Create a data log file called my_file.txt
data = DataLog('time', 'angle', name='my_file', timestamp=False, extension='txt')

# The log method uses the print() method to add a line of text.
# So, you can do much more than saving numbers. For example:
data.log('Temperature', 25)
data.log('Sunday', 'Monday', 'Tuesday')
data.log({'Kiwi': Color.GREEN}, {'Banana': Color.YELLOW})

# You can upload the file to your computer, but you can also print the data:
print(data)
