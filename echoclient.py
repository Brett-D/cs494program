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



def forward():
	conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	conn.connect((host,port))
	_id = str(conn.getsockname()[1])
	return [_id, conn]
	
#network stuff
class Maingame:
	def __init__(self):
		self.me,self.conn = forward()
		self.players = []
		self.players_id = []

if __name__ == "__main__":		
	game = Maingame()
	try:
		#forward()
		#data = raw_input("enter player name:")
		#game.conn.send(data)
		#data = game.conn.recv(size)
		#print 'Received:', data

		while data.strip() != 'quit':
			
			data = raw_input("Enter Direction:")
			
			game.conn.send(data)
			#command = 1
			data = game.conn.recv(size)
			#game.conn.send(NULL)
			#decode(data)
			#game.conn.close()
			#print 'command:' , command
			print 'Received:', data
	finally:
			game.conn.close()
