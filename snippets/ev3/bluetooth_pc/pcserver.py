from pybricks.messaging import BluetoothMailboxServer, TextMailbox

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

print('waiting for connection...')
server.wait_for_connection()
print('connected!')

mbox.wait()
print(mbox.read())
mbox.send('hello to you!')
