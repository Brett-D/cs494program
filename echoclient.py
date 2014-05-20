#!/usr/bin/env python

"""
A simple echo client
"""

import socket
data = 'hello'
host = 'localhost'
port = 50000
size = 1024
#game declerations





#network stuff
while data.strip() != 'quit':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	#s.send('Hello, world')
	s.send(raw_input("enter word:"))
	data = s.recv(size)
	s.close()
	print 'Received:', data
s.close()