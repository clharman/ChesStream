import math

#REQUIRES threshold is positive in pawns, move_number is positive number & 
#	ends in .0 or .5, scores are in pawns.
#EFFECTS  if the score_now is threshold more or less than score_prev,
#	returns who blundered ("Black" or "White"), blunder score differential in pawns
#	(As assessed by the computer), and integer move number.  Otherwise returns 0.
def BlunderCheck(threshold, score_prev, score_now, move_number):

	if(abs(score_prev-score_now) > threshold):
		if(move_number == math.floor(move_number)):
			blunderer = "White"
		else:
			blunderer = "Black"

		diff = abs(score_prev-score_now)
		move = math.floor(move_number)

		return (blunderer, diff, move)
	return 0

#REQUIRES this is used the half-move following BlunderCheck, move_number is positive &
#	ends in .0 or .5, scores are in pawns
#EFFECTS  returns player color and int move if score_now is worse than score_prev 
#	(indicates giving the opponent a chance to un-blunder)
#	("Worse" meaning less in the favor of the current player). Otherwise returns 0.
def CapitalizeCheck(score_prev, score_now, move_number):
	if(move_number == math.floor(move_number)):
		capitalist = "White"
		if(score_now < score_prev):
			return (capitalist, math.floor(move_number))
	else:
		capitalist = "Black"
		if(score_now > score_prev):
			return (capitalist, math.floor(move_number))
	return 0