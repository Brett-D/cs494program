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
		
		data = game.conn.recv(size) #set the character name
		data = raw_input(data)			
		game.conn.send(data)
		data = game.conn.recv(size) #set the x position
		data = raw_input(data)			
		game.conn.send(data)
		data = game.conn.recv(size) #set the y position
		data = raw_input(data)			
		game.conn.send(data)

		while data.strip() != 'quit':
			
			#game.conn.send(data)#check for players
			data = (int)(game.conn.recv(size))
			print "number of players", data
			if data < 2:
				print "waiting for player"
				data = "continue"
				raw_input("continue")
			elif data > 1:
				data = raw_input("Enter Movement:")
				game.conn.send(data)
				xpos = (int)(game.conn.recv(size)) #set the x position
				print "xpos" , xpos
				game.conn.send('1')
				ypos = (int)(game.conn.recv(size)) #set the y position
				print "ypos" , ypos			
				updateLoc(xpos, ypos)
				game.conn.send('1')
			
	finally:
			game.conn.close()
