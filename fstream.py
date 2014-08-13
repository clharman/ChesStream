
#import game.py


#open pgn file to read

username = "clharman"

with open('chess_com_games_(14588528)-2013_12_24_1_19_pm.pgn', 'r') as game:
	#Skip to date line
	for x in range(0, 3):
		line = game.readline()

	#Date in yyyy.mm.dd format:
	date = line[7:len(line)- 3]
	print date

	#White player
	line = game.readline()
	if(line.find(username) > -1):
		color = "white"
		print "Color: " + color

	#Black player
	line = game.readline()
	if(line.find(username) > -1):
		color = "black"
		print "Color: " + color
	else:
		print "Game does not contain username."


	#Result (1-0, 0-1, 1/2-1/2)
	line = game.readline()
	if(line.find("1-0") > -1):
		winner = "white"
	elif(line.find("0-1") > -1):
		winner = "black"
	else:
		winner = "draw"

	if(winner == color):
		result = "win"
	elif(winner == "draw"):
		result = "draw"
	else:
		result = "loss"

	print "Result: " + result

	#White Elo
	line = game.readline()
	elo_white = int(line[11:len(line)- 3])

	#Black Elo
	line = game.readline()
	elo_black = int(line[11:len(line)- 3])

	#elo_my and elo_opponent
	if(color == "white"):
		elo_my = elo_white
		elo_opponent = elo_black
	else:
		elo_my = elo_black
		elo_opponent = elo_white

	print "My rating: " + str(elo_my)
	print "Opponent's rating: " + str(elo_opponent)

	#Time control
	line = game.readline()
	#Throwaway for now

	#Termination condition
	line = game.readline()

	#Empty line
	line = game.readline()

	moves = ""
	while 1:
		line = game.readline().rstrip('\n')
		if not line:
			break
		moves = moves + line

	print moves




game.closed