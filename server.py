# server.py

import socket                   # Import socket module
import hashlib

port = 5103                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = "192.168.248.1"     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    data = conn.recv(1024)
    reqFilename = data.decode('utf-8')
    print 'Requested file name : ', reqFilename
    print hashlib.md5(open(reqFilename, 'rb').read()).hexdigest()

    filename=reqFilename
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       #print 'Sending file...'
       l = f.read(1024)
    f.close()

    print('Done sending. Thank you')
 #   conn.send('Thank you for connecting') to md5
    conn.close()