#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

from pybricks.bluetooth import EV3MailboxClient

# Replace this with the Bluetooth address of the server. This address can be
# found on the screen of the client EV3 after pairing with the server.
SERVER = '00:17:E7:XX:XX:XX'

client = EV3MailboxClient(SERVER)

# The server must be started before the client!
print('establishing connection...')
client.connect()
print('connected!')

# In this program, the client sends the first message and then waits for the
# server to reply.
client.send_text(SERVER, 'msg1', 'hello!')
client.wait_for_update('msg2')
print(client.get_text('msg2'))
