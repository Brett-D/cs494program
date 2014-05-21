#!/usr/bin/env python

"""
A simple echo server
"""

import socket
import select
import sys

host = '' #fill the address to an empty string.
port = 50000 
backlog = 5 #number of clients can have a maximum of 5 waiting connections.
size = 1024

#game board
playerpos_y = 0
playerpos_x = 1
boardsize = 4 #sets the board size
#create matrix for game board
board = [['0']*boardsize for x in range(boardsize)]

def matrix_move(command):
	global board
	global playerpos_x
	global playerpos_y
	global boardsize
	#movecheck
	board[playerpos_x][playerpos_y] = '0'
	if command == 'up':
		print 'moving up'
		#if movecheck == (playerpos_x + 1 >= boardsize):
		
		playerpos_x = playerpos_x - 1
		if playerpos_x < 0:
			playerpos_x = boardsize - 1
		
	elif command == 'down':
		print 'moving down'
		playerpos_x = playerpos_x + 1
		if playerpos_x > boardsize - 1:
			playerpos_x = 0
	elif command == 'left':
		print 'moving left'
		playerpos_y = playerpos_y - 1
		if playerpos_y < 0:
			playerpos_y = boardsize - 1
	elif command == 'right':
		print 'moving right'
		playerpos_y = playerpos_y + 1
		if playerpos_y > boardsize - 1:
			playerpos_y = 0
	else:
		print 'invalid move'
	board[playerpos_x][playerpos_y] ='@'
#game stuff

def printBoard(uboard):
	print' ',
	for x in range(len(board[1])): 
		print x,
	print
	for x, element in enumerate(uboard):
		print x, ' '.join(element)
	



#mx = make_gameboard(3,3)
#print board
printBoard(board)

board[playerpos_x][playerpos_y] = '@'

printBoard(board)
#print board

#print(mx)
#mx[3][1] = 1


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port)) #binds the host name to the port
s.listen(backlog) #allows the operating system to keep a backlog of specified backlog
print 'Server Started!'
while 1:
    client, address = s.accept() #accepts the incoming connections.
    data = client.recv(size) # receives the data from client.
    if data: #checks if the data is zero.
		print 'Received:', data
		#print 'command:' , data
		matrix_move(data)
		#print board
		printBoard(board)
		#command = 2
		data = 'p' + str(playerpos_x) + str(playerpos_y)
		client.send(data)
		#client.send(data)#sends the data back that it received.
client.close()