#TO DO
#	Fix blunder and Game and Chessboard to use either "Black" or "B", not both


import Game, time, math
import ChessBoard
import notation_converter

import blunder
from uci_interface import *
username = "clharman"
filename = "chess_com_games_(14588528)-2013_12_24_1_19_pm.pgn"
my_game = Game.Game(username, filename)


chessboard = ChessBoard.ChessBoard()
moveset = notation_converter.moves(my_game.get_moves())

#Convert the moves:
for move in moveset:

	chessboard.addTextMove(move)

moveset = chessboard.getAllTextMoves(chessboard.AN)


print get()
put('uci')
print get()
put('setoption name Hash value 128')
print get()
put('ucinewgame')
print get()


movenum = 1
so_far = ''
for move in moveset:
	#print str(movenum) + ':\t' + move
	
	so_far += move + ' '
	#put('stop')
	put ('position startpos moves ' + so_far)
	put("go movetime 1000")
	#print get()
	#time.sleep()


	
	reply = get()
	score = reply[(reply.find('score cp')+9):reply.find(" ", (reply.find('score cp')+9), len(reply))-1]
	score = score.strip()

	if (score and score == '-'):
		score = 0

	if (math.floor(movenum) != movenum  and score):
		score = float(score) * -1 

	if(score):
		score = float(score) / 10
		print str(movenum) + ":\t" + str(score) + "\t" + move
	else:
		print str(movenum) + ":\t\t" + move
	movenum += 0.5
get()
put('stop')
get()
put('quit')


