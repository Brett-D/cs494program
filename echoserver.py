#!/usr/bin/env python

"""
Written by Brett Dunscomb
This is my python game server called man hunt
The object of this game is to move into the space occupied by the other player
"""

import socket
import select
import sys



host = '' #fill the address to an empty string.
port = 50000 
backlog = 2 #number of clients can have a maximum of 5 waiting connections.
size = 1024

player = {}

#game board

boardsize = 4 #sets the board size
#create matrix for game board
board = [['0']*boardsize for x in range(boardsize)]
numplayer = 0


#def command_decode(command)
	





#game stuff

def printBoard(uboard):
	print' ',
	for x in range(len(board[1])): 
		print x,
	print
	for x, element in enumerate(uboard):
		print x, ' '.join(element)




class manServer:

	def __init__(self, host, port):
			self.input_list = []
			self.players = []			
			self.channel = {}

			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.server.bind((host, port))
			self.server.listen(backlog)

	def wingame(self, playertype, _id):
		print "wingame"
		n_player = playertype.keys()
		n_player1 = n_player[0]
		n_player2 = n_player[1]
		
		c_info1 = playertype[n_player1]
		c_info2 = playertype[n_player2]
		
		#switch players turns
		if c_info1.waiting == "w":
			c_info1.waiting ="N"
			c_info2.waiting ="w"
		else:
			c_info1.waiting ="w"
			c_info2.waiting ="N"
		
		if c_info1.position_X == c_info2.position_X and c_info1.position_Y == c_info2.position_Y:
			if n_player1 == _id:	
				print "lost" , c_info2.name
				c_info2.win = "0"
				c_info1.win = "1"
			if n_player2 == _id:
				print "lost" , c_info1.name
				c_info1.win = "0"
				c_info2.win = "1"



	def messagedecode(self,player_stuff,_id):
		print"in messagedecode"	
		print self.data	
		if self.data[0] == "p":
			print "check player"
			numplayer = len(player)
			player_stuff.socket.send((str)(numplayer) + player_stuff.waiting + player_stuff.win)

		if self.data[0] == "m":
			print "movement"
			self.data = list(self.data)
			del(self.data[0])
			self.data = "".join(self.data)
			self.matrix_move(self.data,player_stuff)
			xpos = (str)(player_stuff.position_X)
			ypos = (str)(player_stuff.position_Y)
			self.wingame(player ,_id)
			player_stuff.socket.send(xpos + ypos) #player response
			player_stuff.wait = "w"
		if self.data[0] == "w":
			print "checking for win and player lock"
			player_stuff.socket.send(player_stuff.waiting + player_stuff.win)
		if self.data[0] == "c":
			print "getting name"
			self.data = list(self.data)
			del(self.data[0])
			self.data = "".join(self.data)
			player_stuff.name = self.data
		if self.data[0] == "]": 
			print "getting X position"
			self.data = list(self.data)
			del(self.data[0])
			self.data = "".join(self.data)
			player_stuff.position_X = (int)(self.data)
		if self.data[0] == "[": 
			print "getting Y position"
			self.data = list(self.data)
			del(self.data[0])
			self.data = "".join(self.data)
			player_stuff.position_Y = (int)(self.data)
			self.setboard(player_stuff);
			player_stuff.socket.send("setting up board")
			
			
			

	
	def setboard(self,Player):
		print "players x position" , Player.position_X
		print "players Y position" , Player.position_Y
		board[Player.position_X][Player.position_Y] = '@'
		
	

	def matrix_move(self,command, Player):
	
		board[Player.position_X][Player.position_Y] = '0'
		if command == 'up':
			print 'moving up'
			#if movecheck == (playerpos_x + 1 >= boardsize):
		
			Player.position_X = Player.position_X - 1
			if Player.position_X < 0:
				Player.position_X = boardsize - 1
		
		elif command == 'down':
			print 'moving down'
			Player.position_X = Player.position_X + 1
			if Player.position_X > boardsize - 1:
				Player.position_X = 0
		elif command == 'left':
			print 'moving left'
			Player.position_Y = Player.position_Y - 1
			if Player.position_Y < 0:
				Player.position_Y = boardsize - 1
		elif command == 'right':
			print 'moving right'
			Player.position_Y = Player.position_Y + 1
			if Player.position_Y > boardsize - 1:
				Player.position_Y = 0
		else:
			print 'invalid move'
		board[Player.position_X][Player.position_Y] ='@'
	

	






	def main_loop(self):
		self.input_list.append(self.server)
		print "server starting"
		while 1:
			print "connected:" ,player
			printBoard(board)			
			#print player[_id]
			inputr,outputr,exceptr = select.select(self.input_list,[],[])
			for self.s in inputr:
				if self.s == self.server:
					self.on_accept()
					break			
				else:
					self.data = self.s.recv(size)
				if not self.data:
					self.on_close()					
				else:
					self.on_recv()
	
	def on_accept(self):
				
		clientsock, clientaddr = self.server.accept() #player connecting
		print len(player)		
		if len(player) > 1:
			clientsock.close()
			print "refusing connection"
			return		
		print clientaddr, "has connected"
			
		#clientsock.send('what is your name?')
		#name = clientsock.recv(size)
		#clientsock.send('X?')
		#X = (int)(clientsock.recv(size))
		#clientsock.send('Y?')
		#Y = (int)(clientsock.recv(size))
		gplayer = Player("none",clientsock,0,0)
		self.players.append(gplayer)
		#print "coonnected player:",gplayer.name
		#print "players:" , self.players
		player[clientaddr[1]] = gplayer
		self.input_list.append(clientsock)
		numplayer = len(player)
		if numplayer > 1:
			gplayer.waiting = "w" #player goes second
		elif numplayer == 1:
			gplayer.waiting = "N" #player goes first
		
		
	def check_player(self):
		clientaddr = self.s.getpeername()
		
	

	def on_close(self):
		#numplayer = numplayer - 1 #keep track of players
		clientaddr = self.s.getpeername()
		_id = self.s.getpeername()[1]
		c_info = player[_id]
		board[c_info.position_X][c_info.position_Y] = '0'		
		print "%s has disconnected" % clientaddr[0]
		del(player[clientaddr[1]])
		self.input_list.remove(self.s)
		
	def on_recv(self):
		
		_id = self.s.getpeername()[1]
		
		c_info = player[_id]
		
		print "in recive"
		self.messagedecode(c_info,_id)		
		
		
		
class Player:

	def __init__(self, name, socket, position_X, position_Y,current_game = None, win = "2", waiting = "N"):
		self.name = name
		self.socket = socket
		self.current_game = current_game
		self.position_X = position_X
		self.position_Y = position_Y
		self.win = win
		self.waiting = waiting

		


if __name__ == '__main__':
	server = manServer(host,port)
	try:
		server.main_loop()
	except KeyboardInterrupt:
		print "stopping server"
		sys.exit(1)









client.close()
