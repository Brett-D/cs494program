#!/usr/bin/env python

"""
A simple echo client
"""

import socket
import select
import sys
import os

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


def updateLoc(xpos, ypos):
	for x in range(boardsize):
		for y in range(boardsize):
			board[x][y] = '0'
	
	board[xpos][ypos] = '@'
	
	os.system('cls' if os.name == 'nt' else 'clear')
	
	printBoard(board)
		
		
#game commands		

def decode(data):
	if data[0] == 'p':
		xpos = data[1]
		ypos = data[2]
		print 'posx:', xpos
		print 'posy:', ypos
		updateLoc(int(xpos), int(ypos))

#network stuff
while data.strip() != 'quit':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	#s.send('Hello, world')
	
	data = raw_input("enter direction:")
	
	s.send(data)
	#command = 1
	data = s.recv(size)
	decode(data)
	s.close()
	#print 'command:' , command
	print 'Received:', data
s.close()