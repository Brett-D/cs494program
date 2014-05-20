#!/usr/bin/env python

"""
A simple echo client
"""

import socket
import select
import sys
data = 'hello'
host = 'localhost'
port = 50000
size = 1024
#game declerations
boardsize = 4

board = [['0']*boardsize for x in range(boardsize)]


#game functions
def printBoard(uboard):
	print' ',
	for x in range(len(board[1])): 
		print x,
	print
	for x, element in enumerate(uboard):
		print x, ' '.join(element)


#game commands		


#network stuff
while data.strip() != 'quit':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	#s.send('Hello, world')
	
	data = raw_input("enter direction:")
	
	s.send({data})
	#command = 1
	data = s.recv(size)
	s.close()
	#print 'command:' , command
	print 'Received:', data[1]
s.close()