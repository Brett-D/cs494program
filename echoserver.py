#!/usr/bin/env python

"""
A simple echo server
"""

import socket
import select
import sys
import thread


host = '' #fill the address to an empty string.
port = 50000 
backlog = 5 #number of clients can have a maximum of 5 waiting connections.
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

	def wingame(self, playertype,_id):
		print "wingame"
		n_player = playertype.keys()
		n_player1 = n_player[0]
		n_player2 = n_player[1]
		
		c_info1 = playertype[n_player1]
		c_info2 = playertype[n_player2]
		
		if c_info1.position_X == c_info2.position_X and c_info1.position_Y == c_info2.position_Y:
			if n_player1 == _id:	
				print "lost" , c_info2.name
			if n_player2 == _id:
				print "lost" , c_info1.name



	def messagedecode(self,player_stuff):
		print"in messagedecode"	
		print self.data	
		if self.data[0] == "p":
			print "check player"
			numplayer = len(player)
			player_stuff.socket.send((str)(numplayer))

		if self.data[0] == "m":
			print "movement"
			self.data = list(self.data)
			del(self.data[0])
			self.data = "".join(self.data)
			self.matrix_move(self.data,player_stuff)
			xpos = (str)(player_stuff.position_X)
			ypos = (str)(player_stuff.position_Y)
			player_stuff.socket.send(xpos + ypos)
			

	
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
		print clientaddr, "has connected"
		clientsock.send('what is your name?')
		name = clientsock.recv(size)
		clientsock.send('X?')
		X = (int)(clientsock.recv(size))
		clientsock.send('Y?')
		Y = (int)(clientsock.recv(size))
		gplayer = Player(name, clientsock, X, Y)
		self.players.append(gplayer)
		print "coonnected player:",gplayer.name
		print "players:" , self.players
		player[clientaddr[1]] = gplayer
		self.input_list.append(clientsock)
		self.setboard(gplayer);
		#print "players x position" , gplayer.position_X
		#print "players Y position" , gplayer.position_Y
		#numplayer =+ 1 #keep track of players
		
		#self.s.send((str)(numplayer))
		
	def check_player(self):
		clientaddr = self.s.getpeername()
		
	

	def on_close(self):
		#numplayer = numplayer - 1 #keep track of players
		clientaddr = self.s.getpeername()
		print "%s has disconnected" % clientaddr[0]
		del(player[clientaddr[1]])
		self.input_list.remove(self.s)
		
	def on_recv(self):
		
		_id = self.s.getpeername()[1]
		#player[_id] = self.data
		#print player[_id]
		c_info = player[_id]
		
		print "in recive"
		self.messagedecode(c_info)		
		
		#data = self.s.recv(size)
		#print "recived",self.data
		#c_info.socket.sendall("2")
		
			#c_info.socket.send("1")
			#c_info.socket.send('what is your quest?')
			#cool = c_info.socket.recv(size)
			#print c_info.socket			
			#c_info.socket.send("1")		
			#command = c_info.socket.recv(size)
			#print "This player moved",c_info.name
			#print "command" ,command		
			#self.matrix_move(command, c_info)
			#printBoard(board)
			#xpos = (str)(c_info.position_X)
			#ypos = (str)(c_info.position_Y)
			#c_info.socket.send(xpos)
			#print "Sent x pos", xpos
			#c_info.socket.recv(size)
			#c_info.socket.send(ypos)		
			#print "sent y pos", ypos
			#self.wingame(player,_id)
			#c_info.socket.recv(size)
		
class Player:

	def __init__(self, name, socket, position_X, position_Y,current_game = None):
		self.name = name
		self.socket = socket
		self.current_game = current_game
		self.position_X = position_X
		self.position_Y = position_Y

		


if __name__ == '__main__':
	server = manServer(host,port)
	try:
		server.main_loop()
	except KeyboardInterrupt:
		print "stopping server"
		sys.exit(1)








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
