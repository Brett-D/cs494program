#!/usr/bin/env python

"""
A simple echo client
"""

import socket
import select
import sys
import os
import time

data = 'hello'
move = 'up'
host = 'localhost'
port = 50000
size = 1024
#game declerations
boardsize = 4
playerlock = 0

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
		
		os.system('cls' if os.name == 'nt' else 'clear')		
		
		data = game.conn.recv(size) #set the character name
		data = raw_input(data)			
		game.conn.send(data)
		data = game.conn.recv(size) #set the x position
		xpos = raw_input(data)			
		game.conn.send(xpos)
		data = game.conn.recv(size) #set the y position
		ypos = raw_input(data)			
		game.conn.send(ypos)
		xpos =(int)(xpos)
		ypos =(int)(ypos)
		
			

		while move.strip() != 'quit':
						
			data = "p" #request connected players
			game.conn.send(data)
			playerlock = (game.conn.recv(size))
			#print playerlock, "bd" #debug message
			if playerlock[2] == "1":
				print "you found your target and winBD"
				game.conn.close()
				quit()
			
			elif playerlock[2] =="0":
				print "you have been found you looseBD"
				game.conn.close()
				quit()			
						
			
			if playerlock[0] == "1":
				print "waiting for player to join"
				move=raw_input("Press Return or type quit")
			elif playerlock[0] == "2" and playerlock[1] == "N":
				#data = game.conn.recv(size)
				updateLoc(xpos,ypos)
				print "two players connected"
				move = raw_input("Enter Movement(up,down,left,right,quit):")
				game.conn.send("m" + move) #sends movement command
				data = game.conn.recv(size)
				xpos = (int)(data[0])
				ypos = (int)(data[1])
				updateLoc(xpos,ypos)
				#print data
			elif playerlock[1] == "w":
					updateLoc(xpos,ypos)
					#print playerlock			
					print "waiting for player"
					time.sleep(1)
							
			
	finally:
			game.conn.close()
