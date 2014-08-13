#REQUIRES moves_short is a string of moves and move numbers seperated by ' ' and '.'
#EFFECTS  returns a (dictionary of moves starting with 1 in steps of .5, the number of moves)
def moves(moves_short):
	moves_short = moves_short.replace(".", " ")
	moveset = []
	for word in moves_short.split(' '):
		if not word[0].isdigit():
			moveset.append(word)
	return moveset