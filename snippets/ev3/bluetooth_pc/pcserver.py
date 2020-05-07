#!/usr/bin/env python3
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

# This demo makes your PC talk to an EV3 over Bluetooth.
#
# Note that is identical to the EV3 server example in ../bluetooth_server
#
# The only difference is that it runs in Python3 on your computer, thanks to
# the Python3 implementation of the messaging module that is included here.
# As far as the EV3 is concerned, it thinks it is just talking to an EV3.
#
# So, the EV3 client example needs no further modifications. The connection
# procedure is also the same as documented in the messaging module docs:
# https://docs.pybricks.com/en/latest/messaging.html
#
# So, turn Bluetooth on on your PC and the EV3 and pair them.
#
# Of course, you'll need to enter your PC Bluetooth name in the EV3 client
# example so the EV3 knows which paired device to connect to. For example,
# change it to say: SERVER = 'work-laptop' if that is the device name.

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

print('waiting for connection...')
server.wait_for_connection()
print('connected!')

mbox.wait()
print(mbox.read())
mbox.send('hello to you!')
