#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

from pybricks.bluetooth import ALL_BRICKS, EV3MailboxServer

server = EV3MailboxServer()

# The server must be started before the client!
print('waiting for connection...')
server.wait_for_connection()
print('connected!')

# In this program, the server waits for the client to send the first message
# and then sends a reply.
server.wait_for_update('msg1')
print(server.get_text('msg1'))
server.send_text(ALL_BRICKS, 'msg2', 'hello to you too!')
