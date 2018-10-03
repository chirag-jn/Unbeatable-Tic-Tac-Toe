#Assignment-2, Game Tic-tac-toe

#State: Tiles are numbered 1 to 9

"""
Tick-Tac-Toe game state is defined as follows: 

tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______

A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.

We will estimate probability of winning for a player for different scenarios.
 
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.

Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.

Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.  
"""

import random 
# There are 2 players: player1 and player2
player1=1
player2=2


# There are 9 tiles numbered tile0 to tile9
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2

#GLOBAL VARIABLES
tile1= 0
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0
tile9= 0

tiley1 = tile1
tiley2 = tile2
tiley3 = tile3
tiley4 = tile4
tiley5 = tile5
tiley6 = tile6
tiley7 = tile7
tiley8 = tile8
tiley9 = tile9

corners = "1379"
sides = "2468"

#FUNCTIONS:

def resetglobal():
	#RESETS THE GLOBAL VARIABLES BACK TO 0
	global tile1
	global tile2
	global tile3
	global tile4
	global tile5
	global tile6
	global tile7
	global tile8
	global tile9

	tile1 = 0
	tile2 = 0
	tile3 = 0
	tile4 = 0
	tile5 = 0
	tile6 = 0
	tile7 = 0
	tile8 = 0
	tile9 = 0

def validmove(move):
	""" Checks whether a move played by a player is valid or invalid.
		Return True if move is valid. 
		
		A move is valid if the corresponding tile for the move is not ticked.
	"""
	global tile1
	global tile2
	global tile3
	global tile4
	global tile5
	global tile6
	global tile7
	global tile8
	global tile9

	if move == 1:
		if tile1 == 0:
			return True
		else:
			return False
	if move == 2:
		if tile2 == 0:
			return True
		else:
			return False
	
	if move == 3:
		if tile3 == 0:
			return True
		else:
			return False
	
	if move == 4:
		if tile4 == 0:
			return True
		else:
			return False
	
	if move == 5:
		if tile5 == 0:
			return True
		else:
			return False
	
	if move == 6:
		if tile6 == 0:
			return True
		else:
			return False
	
	if move == 7:
		if tile7 == 0:
			return True
		else:
			return False
	
	if move == 8:
		if tile8 == 0:
			return True
		else:
			return False
	
	if move == 9:
		if tile9 == 0:
			return True
		else:
			return False

def win():
	""" Returns True if the board state specifies a winning state for some player.
		
		A player wins if ticks made by the player are present either
		i) in a row
		ii) in a cloumn
		iii) in a diagonal
	"""
	if ((tile1 != 0 and tile2 != 0 and tile3 != 0) or (tile4 != 0 and tile5 != 0 and tile6 != 0) or (tile7 != 0 and tile8 != 0 and tile9 != 0) or (tile1 != 0 and tile4 != 0 and tile7 != 0) or (tile2 != 0 and tile5 != 0 and tile8 != 0) or (tile3 != 0 and tile6 != 0 and tile9 != 0) or (tile7 != 0 and tile5 != 0 and tile3 != 0) or (tile1 != 0 and tile5 != 0 and tile9 != 0)):
		return True
	else:
		return False

def winy():
	#CHECKS WHETHER THE WIN CONDITION FOR TEMPORARY VARIABLES 'tiley_'
	global tiley1
	global tiley2
	global tiley3
	global tiley4
	global tiley5
	global tiley6
	global tiley7
	global tiley8
	global tiley9
	if ((tiley1 != 0 and tiley2 != 0 and tiley3 != 0) or (tiley4 != 0 and tiley5 != 0 and tiley6 != 0) or (tiley7 != 0 and tiley8 != 0 and tiley9 != 0) or (tiley1 != 0 and tiley4 != 0 and tiley7 != 0) or (tiley2 != 0 and tiley5 != 0 and tiley8 != 0) or (tiley3 != 0 and tiley6 != 0 and tiley9 != 0) or (tiley7 != 0 and tiley5 != 0 and tiley3 != 0) or (tiley1 != 0 and tiley5 != 0 and tiley9 != 0)):
		return True
	else:
		return False

def winy1():
	#CHECKS WHETHER THE WIN CONDITION FOR PERMANENT VARIABLES 'tiley_' FOR PLAYER 1
	global tile1
	global tile2
	global tile3
	global tile4
	global tile5
	global tile6
	global tile7
	global tile8
	global tile9
	if ((tile1 == 1 and tile2 == 1 and tile3 == 1) or (tile4 == 1 and tile5 == 1 and tile6 == 1) or (tile7 == 1 and tile8 == 1 and tile9 == 1) or (tile1 == 1 and tile4 == 1 and tile7 == 1) or (tile2 == 1 and tile5 == 1 and tile8 == 1) or (tile3 == 1 and tile6 == 1 and tile9 == 1) or (tile7 == 1 and tile5 == 1 and tile3 == 1) or (tile1 == 1 and tile5 == 1 and tile9 == 1)):
		return True
	else:
		return False

def winy2():
	#CHECKS WHETHER THE WIN CONDITION FOR PERMANENT VARIABLES 'tiley_' FOR PLAYER 2
	global tile1
	global tile2
	global tile3
	global tile4
	global tile5
	global tile6
	global tile7
	global tile8
	global tile9
	if ((tile1 == 2 and tile2 == 2 and tile3 == 2) or (tile4 == 2 and tile5 == 2 and tile6 == 2) or (tile7 == 2 and tile8 == 2 and tile9 == 2) or (tile1 == 2 and tile4 == 2 and tile7 == 2) or (tile2 == 2 and tile5 == 2 and tile8 == 2) or (tile3 == 2 and tile6 == 2 and tile9 == 2) or (tile7 == 2 and tile5 == 2 and tile3 == 2) or (tile1 == 2 and tile5 == 2 and tile9 == 2)):
		return True
	else:
		return False

def takeNaiveMove():
	""" Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.    
	"""
	t = False
	while t != True:
		a = random.randint(1,9)
		t = validmove(a)
	return a

def makemoveplayer1(i):
	#MAKES A MOVE FOR TEMPORARY VARIABLES 'tiley_'. CALLED BY takeStrategicMove(), FOR PLAYER 1
	global tiley1
	global tiley2
	global tiley3
	global tiley4
	global tiley5
	global tiley6
	global tiley7
	global tiley8
	global tiley9
	if i == 1:
		tiley1 = 1
	if i == 2:
		tiley2 = 1
	if i == 3:
		tiley3 = 1
	if i == 4:
		tiley4 = 1
	if i == 5:
		tiley5 = 1
	if i == 6:
		tiley6 = 1
	if i == 7:
		tiley7 = 1
	if i == 8:
		tiley8 = 1
	if i == 9:
		tiley9 = 1

def makemoveplayer2(i):
	#MAKES A MOVE FOR TEMPORARY VARIABLES 'tiley_'. CALLED BY takeStrategicMove(), FOR PLAYER 2
	global tiley1
	global tiley2
	global tiley3
	global tiley4
	global tiley5
	global tiley6
	global tiley7
	global tiley8
	global tiley9
	if i == 1:
		tiley1 = 2
	if i == 2:
		tiley2 = 2
	if i == 3:
		tiley3 = 2
	if i == 4:
		tiley4 = 2
	if i == 5:
		tiley5 = 2
	if i == 6:
		tiley6 = 2
	if i == 7:
		tiley7 = 2
	if i == 8:
		tiley8 = 2
	if i == 9:
		tiley9 = 2

def win_player1():
	#CHECKS WHETHER THE WIN CONDITION FOR TEMPORARY VARIABLES 'tiley_' FOR PLAYER 1
	global tiley1
	global tiley2
	global tiley3
	global tiley4
	global tiley5
	global tiley6
	global tiley7
	global tiley8
	global tiley9
	if (tiley1 == 1 and tiley2 == 1 and tiley3 == 1) or (tiley4 == 1 and tiley5 == 1 and tiley6 == 1) or (tiley7 == 1 and tiley8 == 1 and tiley9 ==1) or (tiley1 ==1 and tiley4 ==1 and tiley7 ==1) or (tiley2 ==1 and tiley5 ==1 and tiley8 ==1) or (tiley3 ==1 and tiley6 ==1 and tiley9 ==1) or (tiley7 ==1 and tiley5 ==1 and tiley3 ==1) or (tiley1 ==1 and tiley5 ==1 and tiley9 ==1):
		return True
	else:
		return False

def win_player2():
	#CHECKS WHETHER THE WIN CONDITION FOR TEMPORARY VARIABLES 'tiley_' FOR PLAYER 2
	global tiley1
	global tiley2
	global tiley3
	global tiley4
	global tiley5
	global tiley6
	global tiley7
	global tiley8
	global tiley9
	if (tiley1 == 2 and tiley2 == 2 and tiley3 == 2) or (tiley4 == 2 and tiley5 == 2 and tiley6 == 2) or (tiley7 == 2 and tiley8 == 2 and tiley9 ==2) or (tiley1 ==2 and tiley4 ==2 and tiley7 ==2) or (tiley2 ==2 and tiley5 ==2 and tiley8 ==2) or (tiley3 ==2 and tiley6 ==2 and tiley9 ==2) or (tiley7 ==2 and tiley5 ==2 and tiley3 ==2) or (tiley1 ==2 and tiley5 ==2 and tiley9 ==2):
		return True
	else:
		return False

def takeStrategicMove():
	""" Returns a tile number from the set of unchecked tiles
	using some rules.
	"""
	"""
	The rules are as follows:
	1. Check if the player can win in the next move or not, if yes, return that number.
	2. Check if the opponent can win in the next move, if yes, return that number.
	3. Occupy the corners, going like: 1-3-7-9
	4. Occupy the middle position, going like: 5
	5. Occupy the sides going like: 2-4-6-8
	"""
	global tiley1
	global tiley2
	global tiley3
	global tiley4
	global tiley5
	global tiley6
	global tiley7
	global tiley8
	global tiley9
		
	#To ckeck whether the AI wins in the next move or it can block the opponent's move so that it cannot lose.
	for i in range(1,10):
		tiley1 = tile1
		tiley2 = tile2
		tiley3 = tile3
		tiley4 = tile4
		tiley5 = tile5
		tiley6 = tile6
		tiley7 = tile7
		tiley8 = tile8
		tiley9 = tile9
		if validmove(i):
			makemoveplayer2(i)
			if win_player2():
				return i
	for i in range(1,10):
		tiley1 = tile1
		tiley2 = tile2
		tiley3 = tile3
		tiley4 = tile4
		tiley5 = tile5
		tiley6 = tile6
		tiley7 = tile7
		tiley8 = tile8
		tiley9 = tile9
		if validmove(i):
			makemoveplayer1(i)
			if win_player1():
				return i

	if tile1 != 0 or tile3 != 0 or tile7 != 0 or tile9 != 0:
		if validmove(5):
			return 5

	for i in corners:
		i = int(i)
		if validmove(i):
			return i
	if validmove(5):
		return 5
	for i in sides:
		i = int(i)
		if validmove(i):
			return i
	
def validBoard():
	""" Return True if board state is valid.
		
		A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
	"""
	sum_of_playa_1 = 0
	sum_of_playa_2 = 0
	if tile1 == player1:
		sum_of_playa_1 += 1
	elif tile1 == player2:
		sum_of_playa_2 += 1

	if tile2 == player1:
		sum_of_playa_1 += 1
	elif tile2 == player2:
		sum_of_playa_2 += 1

	if tile3 == player1:
		sum_of_playa_1 += 1
	elif tile3 == player2:
		sum_of_playa_2 += 1

	if tile4 == player1:
		sum_of_playa_1 += 1
	elif tile4 == player2:
		sum_of_playa_2 += 1

	if tile5 == player1:
		sum_of_playa_1 += 1
	elif tile5 == player2:
		sum_of_playa_2 += 1

	if tile6 == player1:
		sum_of_playa_1 += 1
	elif tile6 == player2:
		sum_of_playa_2 += 1

	if tile7 == player1:
		sum_of_playa_1 += 1
	elif tile7 == player2:
		sum_of_playa_2 += 1

	if tile8 == player1:
		sum_of_playa_1 += 1
	elif tile8 == player2:
		sum_of_playa_2 += 1

	if tile9 == player1:
		sum_of_playa_1 += 1
	elif tile9 == player2:
		sum_of_playa_2 += 1

	if (sum_of_playa_2 == sum_of_playa_1) or ((sum_of_playa_1 - 1) == sum_of_playa_2):
		return True
	else:
		return False
	
def game(gametype=1):
	""" Returns 1 if player1 wins and 2 if player2 wins
		and 0 if it is a draw.
	
		gametype defines three types of games discussed above.
		i.e., game1, game2, game3
	"""
	i = 0
	c = 0
	global tile1
	global tile2
	global tile3
	global tile4
	global tile5
	global tile6
	global tile7
	global tile8
	global tile9
	turn = player1
	if gametype == 1:
		while (winy1() != True) and (winy2() != True) and c != 9:
			i = takeNaiveMove()
			if i == 1:
				tile1 = turn
			elif i == 2:
				tile2 = turn
			elif i == 3:
				tile3 = turn
			elif i == 4:
				tile4 = turn
			elif i == 5:
				tile5 = turn
			elif i == 6:
				tile6 = turn
			elif i == 7:
				tile7 = turn
			elif i == 8:
				tile8 = turn
			elif i == 9:
				tile9 = turn
			turn += 1
			if turn >2:
				turn -= 2
			c += 1
		if winy1():
			resetglobal()
			return 1
		elif winy2():
			resetglobal()
			return 2
		else:
			resetglobal()
			return 0
	elif gametype == 2:
		while (winy1() != True) and (winy2() != True) and c < 9:
			if c%2 == 0:
				i = takeNaiveMove()
			else:
				i = takeStrategicMove()
			#print(i,"move")
			if i == 1:
				tile1 = turn
			elif i == 2:
				tile2 = turn
			elif i == 3:
				tile3 = turn
			elif i == 4:
				tile4 = turn
			elif i == 5:
				tile5 = turn
			elif i == 6:
				tile6 = turn
			elif i == 7:
				tile7 = turn
			elif i == 8:
				tile8 = turn
			elif i == 9:
				tile9 = turn
			turn += 1
			if turn >2:
				turn -= 2
			c += 1
		if winy1():
			resetglobal()
			return 1
		elif winy2():
			resetglobal()
			return 2
		else:
			resetglobal()
			return 0
	elif gametype == 3:
		while (winy1() != True) and (winy2() != True) and c < 9:
			i = takeStrategicMove()
			#print("move",i)
			if i == 1:
				tile1 = turn
			elif i == 2:
				tile2 = turn
			elif i == 3:
				tile3 = turn
			elif i == 4:
				tile4 = turn
			elif i == 5:
				tile5 = turn
			elif i == 6:
				tile6 = turn
			elif i == 7:
				tile7 = turn
			elif i == 8:
				tile8 = turn
			elif i == 9:
				tile9 = turn
			turn += 1
			if turn >2:
				turn -= 2
			c += 1
		if winy1():
			resetglobal()
			return 1
		elif winy2():
			resetglobal()
			return 2
		else:
			resetglobal()
			return 0

def game1(n):
	""" Returns the winning probability for player1. 
	
	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	p1 = 0
	for i in range(n):
		a = game()
		if a == 1:
			p1 += 1
	prob = p1/n
	return prob

def game2(n):

	"""Returns the winning probability for player1.
	
	n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
	"""
	p1 = 0
	for i in range(n):
		a = game(2)
		if a == 1:
			p1 += 1
	prob = p1/n
	return prob

def game3(n):
	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	p1 = 0
	for i in range(n):
		a = game(3)
		if a == 1:
			p1 += 1
	prob = p1/n
	return prob
