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

player = {}
#game board
playerpos_y = 0
playerpos_x = 1
boardsize = 4 #sets the board size
#create matrix for game board
board = [['0']*boardsize for x in range(boardsize)]

class manServer:

	def __init__(self, host, port):
			self.input_list = []
			self.channel = {}

			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.server.bind((host, port))
			self.server.listen(200)
	
	def main_loop(self):
		self.input_list.append(self.server)
		print "server starting"
		while 1:
			print "connected:" ,player
			print player[_id]
			inputr,outputr,exceptr = select.select(self.input_list,[],[])
			for self.s in inputr:
				if self.s == self.server:
					self.on_accept()
					break
				else:
					self.data = self.s.recv(size)
				if (self.data) == "0":
					self.on_close()
				else:
					self.on_recv()
	def on_accept(self):
		clientsock, clientaddr = self.server.accept() #player connecting
		print clientaddr, "has connected"
		player[clientaddr[1]] = {}
		self.input_list.append(clientsock)
	
	def on_close(self):
		clientaddr = self.s.getpeername()
		print "%s has disconnected" % clientaddr[0]
		print "%s has sock" % clientaddr[0]
		del(player[clientaddr[1]])
		self.input_list.remove(self.s)
		
	def on_recv(self):
		_id = self.s.getpeername()[1]
		player[_id] = self.data
		print player[_id]
		self.s.sendall(player[_id]+"\n")
		


if __name__ == '__main__':
	server = manServer(host,port)
	try:
		server.main_loop()
	except KeyboardInterrupt:
		print "stopping server"
		sys.exit(1)





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
