#!/usr/bin/env python

"""
A simple echo server
"""

import socket

host = '' #fill the address to an empty string.
port = 50000 
backlog = 5 #number of clients can have a maximum of 5 waiting connections.
size = 1024

#game board
playerpos_y = 0
playerpos_x = 1
boardsize = 3 #sets the board size
#create matrix for game board
board = [[0 for x in xrange(boardsize)] for x in xrange(boardsize)]

def matrix_move(command):
	global board
	global playerpos_x
	global playerpos_y
	global boardsize
	movecheck
	if command == 'up':
		print 'moving up'
		if movecheck = playerpos_x + 1 >= boardsize || => 0:
		board[playerpos_x][playerpos_y] = 0
		playerpos_x = playerpos_x + 1
		board[playerpos_x][playerpos_y] = 1
	elif command == 'down':
		print 'moving down'
		board[playerpos_x][playerpos_y] = 0
		playerpos_x = playerpos_x - 1
		board[playerpos_x][playerpos_y] = 1
	elif command == 'left':
		print 'moving left'
	elif command == 'right':
		print 'moving right'
		board[playerpos_x][playerpos_y] = 0
		playerpos_y = playerpos_y + 1
		board[playerpos_x][playerpos_y] = 1
	else:
		print 'invalid move'
#game stuff

#mx = make_gameboard(3,3)
print board

board[playerpos_x][playerpos_y] = 1

print board

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
		matrix_move(data)
		print board
		client.send(data)#sends the data back that it received.
client.close()