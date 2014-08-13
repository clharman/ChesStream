#TO DO
#	make elo variables local using __-


class Game:
	'''A game of chess'''


	#All get functions return desired variable
	def get_date(self):
		return self.__date
	def get_moves(self):
		return self.__moves
	def get__color(self):
		return self.__color
	def get_winner(self):
		return self.__winner
	def get_result(self):
		return self.__result
	def get_elo(self, whose):	#whose = 'my', 'opponent', 'white', or 'black'
		return eval("self.elo_" + whose)



	#REQUIRES username and filename are strings 
	#	and filename points to a pgn file
	#	and pgn file is in chess.com format
	#EFFECTS creates new Game object according to pgn file
	def __init__(self, username, filename):
		#open pgn file to read

		with open(filename, 'r') as pgn:
			#Skip to date line
			for x in range(0, 3):
				line = pgn.readline()

			#Date in yyyy.mm.dd format:
			self.__date = line[7:len(line) - 3]

			#White player
			line = pgn.readline()
			if(line.find(username) > -1):
				self.__color = "white"

			#Black player
			line = pgn.readline()
			if(line.find(username) > -1):
				self.__color = "black"
			else:
				self.__color = "null"

			#Result (1-0, 0-1, 1/2-1/2)
			line = pgn.readline()
			if(line.find("1-0") > -1):
				self.__winner = "white"
			elif(line.find("0-1") > -1):
				self.__winner = "black"
			else:
				self.__winner = "draw"

			if(self.__color == "null"):
				self.__result = "null -- wrong username"
			elif(self.__winner == self.__color):
				self.__result = "win"
			elif(self.__winner == "draw"):
				self.__result = "draw"
			else:
				self.__result = "loss"

			#White Elo
			line = pgn.readline()
			self.elo_white = int(line[11:len(line)- 3])

			#Black Elo
			line = pgn.readline()
			self.elo_black = int(line[11:len(line)- 3])

			#__elo_my and __elo_opponent
			if(self.__color == "white"):
				self.elo_my = self.elo_white
				self.elo_opponent = self.__elo_black
			else:
				self.elo_my = self.elo_black
				self.elo_opponent = self.elo_white

			#Time control
			line = pgn.readline()
			#Throwaway for now

			#Termination condition
			line = pgn.readline()

			#Empty line
			line = pgn.readline()

			self.__moves = ""
			
			#__Moves, removing whitespace
			while 1:
				line = pgn.readline().rstrip('\n')
				if not line:
					break
				self.__moves = self.__moves + line

		pgn.closed