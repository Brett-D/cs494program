#!/usr/bin/env python

"""
Written by Brett Dunscomb
This is the game client for the game manhunt
The object of the game is to move into the space occupied by the other player
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
	
	board[xpos][ypos] = 'X'
	
	os.system('cls' if os.name == 'nt' else 'clear')
	
	printBoard(board)
		
		
#game commands		



def forward():
	try:
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.connect((host,port))
		
	except socket.error, (value,message):
    		if conn:
        		conn.close()
   			print "Could not open socket: " + message
    			sys.exit(1) 
	_id = str(conn.getsockname()[1])
	return [_id, conn]

def RepresentsInt(s):
    	try: 
        	s = int(s)
		if s > boardsize - 1:
			return False
		else:
			return True
    	except ValueError:
        	return False

	
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
		
		#data = game.conn.recv(size) #set the character name
		start = raw_input("Enter your players name")			
		game.conn.send("c" + start)
		#data = game.conn.recv(size) #set the x position
		while True:		
			xpos = raw_input("Enter your x starting position")			
			cont = RepresentsInt(xpos)
			if cont:
				break		
		game.conn.send("]" + xpos)
		#data = game.conn.recv(size) #set the y position
		while True:
			ypos = raw_input("Enter your y starting position")			
			cont = RepresentsInt(ypos)
			if cont:
				break				
		game.conn.send("[" + ypos)
		xpos =(int)(xpos)
		ypos =(int)(ypos)
		start = game.conn.recv(size)
		print start	

		while move.strip() != 'quit':
			try:			
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
						
			
				if playerlock[0] == "2" and playerlock[1] == "N":
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
				elif playerlock[1] == "w" or playerlock[0] == "1":
						updateLoc(xpos,ypos)
						#print playerlock			
						print "waiting for player"
						time.sleep(1)
			except socket.error, (value,message):
    				if game.conn:
        				game.conn.close()
   					print "Server error: " + message
    					sys.exit(1) 
							
			
	finally:
			game.conn.close()
