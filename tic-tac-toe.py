# Name: Chirag Jain
# Roll No: 2017041
# Assignment: Tic Tac Toe Game
# File Name: a2.py

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
import tile as t # tile.py contains all info about our tiles

# All data related to the players and tiles have been moved to another file named data.py
"""
# There are 2 players: player1 and player2
player1=1
player2=2
"""

# There are 9 tiles numbered tile0 to tile9
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2

"""
tile1= 0    
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0
tile9= 0
"""

# turn variable defines whose turn is now
#turn = Player1

def validmove(move):
	""" Checks whether a move played by a player is valid or invalid.
		Return True if move is valid. 
		
		A move is valid if the corresponding tile for the move is not ticked.
	"""
	if (move==1):
		if(t.tile1!=0):
			return False
		return True
	if (move==2):
		if(t.tile2!=0):
			return False
		return True
	if (move==3):
		if(t.tile3!=0):
			return False
		return True
	if (move==4):
		if(t.tile4!=0):
			return False
		return True
	if (move==5):
		if(t.tile5!=0):
			return False
		return True
	if (move==6):
		if(t.tile6!=0):
			return False
		return True
	if (move==7):
		if(t.tile7!=0):
			return False
		return True
	if (move==8):
		if(t.tile8!=0):
			return False
		return True
	if (move==9):
		if(t.tile9!=0):
			return False
		return True  

def win(): 
	""" Returns True if the board state specifies a winning state for some player.
		
		A player wins if ticks made by the player are present either
		i) in a row
		ii) in a cloumn
		iii) in a diagonal
	"""
	if(t.tile1==t.tile2==t.tile3>0 or t.tile4==t.tile5==t.tile6>0 or t.tile7==t.tile8==t.tile9>0 or t.tile1==t.tile4==t.tile7>0 or t.tile2==t.tile5==t.tile8>0 or t.tile3==t.tile6==t.tile9>0 or t.tile1==t.tile5==t.tile9>0 or t.tile3==t.tile5==t.tile7>0):
		return True
	return False
	
def takeNaiveMove(): 
	""" Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.    
	"""
	flag=0
	for i in range(9):
		num=random.randint(1,9)
		if(num==1 and t.tile1==0):
			flag=1
			return num
		if(num==2 and t.tile2==0):
			flag=1
			return num
		if(num==3 and t.tile3==0):
			flag=1
			return num
		if(num==4 and t.tile4==0):
			flag=1
			return num
		if(num==5 and t.tile5==0):
			flag=1
			return num
		if(num==6 and t.tile6==0):
			flag=1
			return num
		if(num==7 and t.tile7==0):
			flag=1
			return num
		if(num==8 and t.tile8==0):
			flag=1
			return num
		if(num==9 and t.tile9==0):
			flag=1
			return num
	if(flag==0):
		return(takeNaiveMove())


def takeStrategicMove(): 
	""" Returns a tile number from the set of unchecked tiles
	using some rules.
	"""
	turn2=0
	if(t.turn==1): turn2=2
	else: turn2=1
	
	# completing own line
	if  (t.tile1==t.turn and t.tile2==t.turn and t.tile3==0): return 3
	elif(t.tile2==t.turn and t.tile3==t.turn and t.tile1==0): return 1
	elif(t.tile3==t.turn and t.tile1==t.turn and t.tile2==0): return 2

	if  (t.tile4==t.turn and t.tile5==t.turn and t.tile6==0): return 6
	elif(t.tile5==t.turn and t.tile6==t.turn and t.tile4==0): return 4
	elif(t.tile6==t.turn and t.tile4==t.turn and t.tile5==0): return 5

	if  (t.tile7==t.turn and t.tile8==t.turn and t.tile9==0): return 9
	elif(t.tile8==t.turn and t.tile9==t.turn and t.tile7==0): return 7
	elif(t.tile9==t.turn and t.tile7==t.turn and t.tile8==0): return 8

	if  (t.tile1==t.turn and t.tile4==t.turn and t.tile7==0): return 7
	elif(t.tile4==t.turn and t.tile7==t.turn and t.tile1==0): return 1
	elif(t.tile7==t.turn and t.tile1==t.turn and t.tile4==0): return 4

	if  (t.tile2==t.turn and t.tile5==t.turn and t.tile8==0): return 8
	elif(t.tile5==t.turn and t.tile8==t.turn and t.tile2==0): return 2
	elif(t.tile8==t.turn and t.tile2==t.turn and t.tile5==0): return 5

	if  (t.tile3==t.turn and t.tile6==t.turn and t.tile9==0): return 9
	elif(t.tile6==t.turn and t.tile9==t.turn and t.tile3==0): return 3
	elif(t.tile9==t.turn and t.tile3==t.turn and t.tile6==0): return 6

	if  (t.tile1==t.turn and t.tile5==t.turn and t.tile9==0): return 9
	elif(t.tile5==t.turn and t.tile9==t.turn and t.tile1==0): return 1
	elif(t.tile9==t.turn and t.tile1==t.turn and t.tile5==0): return 5

	if  (t.tile3==t.turn and t.tile5==t.turn and t.tile7==0): return 7
	elif(t.tile5==t.turn and t.tile7==t.turn and t.tile3==0): return 3
	elif(t.tile7==t.turn and t.tile3==t.turn and t.tile5==0): return 5

	# capturing other's line
	if  (t.tile1==turn2 and t.tile2==turn2 and t.tile3==0): return 3
	elif(t.tile2==turn2 and t.tile3==turn2 and t.tile1==0): return 1
	elif(t.tile3==turn2 and t.tile1==turn2 and t.tile2==0): return 2

	if  (t.tile4==turn2 and t.tile5==turn2 and t.tile6==0): return 6
	elif(t.tile5==turn2 and t.tile6==turn2 and t.tile4==0): return 4
	elif(t.tile6==turn2 and t.tile4==turn2 and t.tile5==0): return 5

	if  (t.tile7==turn2 and t.tile8==turn2 and t.tile9==0): return 9
	elif(t.tile8==turn2 and t.tile9==turn2 and t.tile7==0): return 7
	elif(t.tile9==turn2 and t.tile7==turn2 and t.tile8==0): return 8

	if  (t.tile1==turn2 and t.tile4==turn2 and t.tile7==0): return 7
	elif(t.tile4==turn2 and t.tile7==turn2 and t.tile1==0): return 1
	elif(t.tile7==turn2 and t.tile1==turn2 and t.tile4==0): return 4

	if  (t.tile2==turn2 and t.tile5==turn2 and t.tile8==0): return 8
	elif(t.tile5==turn2 and t.tile8==turn2 and t.tile2==0): return 2
	elif(t.tile8==turn2 and t.tile2==turn2 and t.tile5==0): return 5

	if  (t.tile3==turn2 and t.tile6==turn2 and t.tile9==0): return 9
	elif(t.tile6==turn2 and t.tile9==turn2 and t.tile3==0): return 3
	elif(t.tile9==turn2 and t.tile3==turn2 and t.tile6==0): return 6

	if  (t.tile1==turn2 and t.tile5==turn2 and t.tile9==0): return 9
	elif(t.tile5==turn2 and t.tile9==turn2 and t.tile1==0): return 1
	elif(t.tile9==turn2 and t.tile1==turn2 and t.tile5==0): return 5

	if  (t.tile3==turn2 and t.tile5==turn2 and t.tile7==0): return 7
	elif(t.tile5==turn2 and t.tile7==turn2 and t.tile3==0): return 3
	elif(t.tile7==turn2 and t.tile3==turn2 and t.tile5==0): return 5

	# for the first move, always must be at corner	
	if(t.tile1==t.tile2==t.tile3==t.tile4==t.tile5==t.tile6==t.tile7==t.tile8==t.tile9==0):
		four_choose=random.randint(1,4)
		if(four_choose==1):	
			return 1
		elif(four_choose==2):
			return 3
		elif(four_choose==3):
			return 7
		elif(four_choose==4):
			return 9
	

	# capturing center if other player puts at corner first
	if(t.tile1==turn2 and t.tile2==t.tile3==t.tile4==t.tile5==t.tile6==t.tile7==t.tile8==t.tile9==0): return 5
	elif(t.tile3==turn2 and t.tile1==t.tile2==t.tile4==t.tile5==t.tile6==t.tile7==t.tile8==t.tile9==0):	return 5
	elif(t.tile7==turn2 and t.tile1==t.tile2==t.tile3==t.tile4==t.tile5==t.tile6==t.tile8==t.tile9==0):	return 5
	elif(t.tile9==turn2 and t.tile1==t.tile2==t.tile3==t.tile4==t.tile5==t.tile6==t.tile7==t.tile8==0):	return 5

	# this case is eventually when tile 5 is taken by the other player while all other are empty
	if(t.tile5==turn2 and t.tile1==t.tile2==t.tile3==t.tile4==t.tile6==t.tile7==t.tile8==t.tile9==0): return(takeNaiveMove())
	
	# if other player plays first at pos 2,4,6,8
	if(t.tile2==turn2 and t.tile1==t.tile3==t.tile4==t.tile5==t.tile6==t.tile7==t.tile8==t.tile9==0): return 5
	elif(t.tile4==turn2 and t.tile1==t.tile2==t.tile3==t.tile5==t.tile6==t.tile7==t.tile8==t.tile9==0):	return 5
	elif(t.tile6==turn2 and t.tile1==t.tile2==t.tile3==t.tile4==t.tile5==t.tile7==t.tile8==t.tile9==0):	return 5
	elif(t.tile8==turn2 and t.tile1==t.tile2==t.tile3==t.tile4==t.tile5==t.tile6==t.tile7==t.tile9==0):	return 5

	# capturing a corner if other player also has a corner and we have the center
	if(t.tile1==turn2 and t.tile5==t.turn and t.tile3==0 and t.tile7==0): return 3
	elif(t.tile3==turn2 and t.tile5==t.turn and t.tile1==0 and t.tile9==0): return 1
	elif(t.tile7==turn2 and t.tile5==t.turn and t.tile1==0 and t.tile9==0): return 1
	elif(t.tile7==turn2 and t.tile5==t.turn and t.tile9==0 and t.tile1==0): return 9
	elif(t.tile9==turn2 and t.tile5==t.turn and t.tile3==0 and t.tile7==0): return 3
	#elif(t.tile5==0): return 5
	
	# if the case was like t.tile9==turn2 and t.tile5==t.turn and t.tile3==0 and t.tile7==t.turn then automatically handled above
	#if(t.tile1==turn2 and t.tile5==t.turn and t.tile3==0 and t.tile7==0): return 3
	#elif(t.tile1==turn2 and t.tile5==t.turn and t.tile7==0 and t.tile3==0): return 7	
	# if both the above conditions fail, then our player is fixed in triangle, will lose for sure

	elif((t.tile2==turn2 or t.tile4==turn2 or t.tile6==turn2 or t.tile8==turn2) and t.tile5==0): return 5
	elif(t.tile2==turn2 and t.tile1==0): return 1
	elif(t.tile2==turn2 and t.tile3==0): return 3
	elif(t.tile4==turn2 and t.tile1==0): return 1
	elif(t.tile4==turn2 and t.tile7==0): return 7
	elif(t.tile6==turn2 and t.tile3==0): return 3
	elif(t.tile6==turn2 and t.tile9==0): return 9
	elif(t.tile8==turn2 and t.tile7==0): return 7
	elif(t.tile8==turn2 and t.tile9==0): return 9
	
	elif((t.tile1==t.turn and t.tile3==0)): return 3
	elif((t.tile4==t.turn and t.tile6==0)): return 6
	elif((t.tile7==t.turn and t.tile9==0)): return 9
	elif((t.tile1==t.turn and t.tile7==0)): return 7
	elif((t.tile2==t.turn and t.tile8==0)): return 8
	elif((t.tile3==t.turn and t.tile9==0)): return 9
	elif((t.tile3==t.turn and t.tile1==0)): return 1
	elif((t.tile6==t.turn and t.tile4==0)): return 4
	elif((t.tile9==t.turn and t.tile7==0)): return 7
	elif((t.tile7==t.turn and t.tile1==0)): return 1
	elif((t.tile8==t.turn and t.tile2==0)): return 2
	elif((t.tile9==t.turn and t.tile3==0)): return 3

	return (takeNaiveMove())

def validBoard(): 
	""" Return True if board state is valid.
		
		A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
	"""
	sum1=0
	sum2=0
	if(t.tile1==1): sum1+=1
	elif(t.tile1==2): sum2+=1
	if(t.tile2==1): sum1+=1
	elif(t.tile2==2): sum2+=1
	if(t.tile3==1): sum1+=1
	elif(t.tile3==2): sum2+=1
	if(t.tile4==1): sum1+=1
	elif(t.tile4==2): sum2+=1
	if(t.tile5==1): sum1+=1
	elif(t.tile5==2): sum2+=1
	if(t.tile6==1): sum1+=1
	elif(t.tile6==2): sum2+=1
	if(t.tile7==1): sum1+=1
	elif(t.tile7==2): sum2+=1
	if(t.tile8==1): sum1+=1
	elif(t.tile8==2): sum2+=1
	if(t.tile9==1): sum1+=1
	elif(t.tile9==2): sum2+=1
	
	if(sum1==sum2 or sum1==sum2+1):
		return True
	return False

def game(gametype=1): 
	""" Returns 1 if player1 wins and 2 if player2 wins
		and 0 if it is a draw.
	
		gametype defines three types of games discussed above.
		i.e., game1, game2, game3
	"""
	if(t.tile1==t.tile2==t.tile3==1 or t.tile4==t.tile5==t.tile6==1 or t.tile7==t.tile8==t.tile9==1 or t.tile1==t.tile4==t.tile7==1 or t.tile2==t.tile5==t.tile8==1 or t.tile3==t.tile6==t.tile9==1 or t.tile1==t.tile5==t.tile9==1 or t.tile3==t.tile5==t.tile7==1):
		return 1
	if(t.tile1==t.tile2==t.tile3==2 or t.tile4==t.tile5==t.tile6==2 or t.tile7==t.tile8==t.tile9==2 or t.tile1==t.tile4==t.tile7==2 or t.tile2==t.tile5==t.tile8==2 or t.tile3==t.tile6==t.tile9==2 or t.tile1==t.tile5==t.tile9==2 or t.tile3==t.tile5==t.tile7==2):
		return 2	
	return 0

def resetgame():
	t.tile1=0
	t.tile2=0
	t.tile3=0
	t.tile4=0
	t.tile5=0
	t.tile6=0
	t.tile7=0
	t.tile8=0
	t.tile9=0

def game1(n):
	""" Returns the winning probability for player1. 
	
	n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	count=0
	for i in range(n):
		resetgame()
		for i in range(9):
			if(i%2==0):
				t.turn=t.Player1
			else:
				t.turn=t.Player2
			taketile=takeNaiveMove()
			if(validmove(taketile)==True):
				if(taketile==1):
					t.tile1+=t.turn
				elif(taketile==2):
					t.tile2+=t.turn
				elif(taketile==3): 
					t.tile3+=t.turn
				elif(taketile==4):
					t.tile4+=t.turn
				elif(taketile==5):
					t.tile5+=t.turn
				elif(taketile==6):
					t.tile6+=t.turn
				elif(taketile==7):
					t.tile7+=t.turn
				elif(taketile==8):
					t.tile8+=t.turn
				elif(taketile==9):
					t.tile9+=t.turn
			if(win()==True):
				if(game(gametype=1)==1):
					count+=1
				break
	return count/n

def game2(n):
	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	Player 1 is a naive player, while Player 2 is intelligent.
	"""
	count=0
	count2=0
	taketile=0
	for i in range(n):
		#print('game2',i)
		resetgame()
		for i in range(9):
			if(i%2==0):
				t.turn=t.Player1
				taketile=takeNaiveMove()
			else:
				t.turn=t.Player2
				taketile=takeStrategicMove()
			if(validmove(taketile)==True):
				if(taketile==1):
					t.tile1+=t.turn
				elif(taketile==2):
					t.tile2+=t.turn
				elif(taketile==3):
					t.tile3+=t.turn
				elif(taketile==4):
					t.tile4+=t.turn
				elif(taketile==5):
					t.tile5+=t.turn
				elif(taketile==6):
					t.tile6+=t.turn
				elif(taketile==7):
					t.tile7+=t.turn
				elif(taketile==8):
					t.tile8+=t.turn
				elif(taketile==9):
					t.tile9+=t.turn
			if(win()==True):
				if(game(gametype=1)==1):
					count+=1
				break
	return count/n

def game3(n):
	"""Returns the winning probability for player1. 
	
	n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
	"""
	count=0
	for i in range(n):
		resetgame()
		for i in range(9):
			if(i%2==0):
				t.turn=t.Player1
			else:
				t.turn=t.Player2
			taketile=takeStrategicMove()
			if(validmove(taketile)==True):
				if(taketile==1):
					t.tile1+=t.turn
				elif(taketile==2):
					t.tile2+=t.turn
				elif(taketile==3):
					t.tile3+=t.turn
				elif(taketile==4):
					t.tile4+=t.turn
				elif(taketile==5):
					t.tile5+=t.turn
				elif(taketile==6):
					t.tile6+=t.turn
				elif(taketile==7):
					t.tile7+=t.turn
				elif(taketile==8):
					t.tile8+=t.turn
				elif(taketile==9):
					t.tile9+=t.turn
			if(win()==True):
				if(game(gametype=1)==1):
					count+=1
				break
	return count/n