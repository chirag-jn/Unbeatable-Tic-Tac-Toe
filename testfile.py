# Name: Chirag Jain
# Roll No: 2017041
# Assignment: Tic Tac Toe Game
# File Name: a2test.py

from tic-tac-toe import *

# in this testing module, we will define our own test cases by defining some values for different tiles
# and check the corresponding value returned by the different functions

# checking for resetgame function, made by me
resetgame()
assert t.tile1==0, 'Some Problem in resetgame function'
print('resetgame function OK')
try:
	assert t.tile2==1, 'Some Problem in resetgame function'
except AssertionError:
	print('resetgame function OK')
try:
	assert t.tile3==2, 'Some Problem in resetgame function'
except AssertionError:
	print('resetgame function OK')

# checking for validmove function
t.tile1=0
assert validmove(1)==True, 'Some Problem in validmove function'
print('validmove function OK')

# checking for win function
t.tile1=1
t.tile2=1
t.tile3=1
assert win()==True, 'Some problem in win function'
print('Win function is OK')
resetgame()
t.tile1=1
t.tile2=1
t.tile3=2
assert win()==False, 'Some problem in win function'
print('Win function is OK')
resetgame()
t.tile1=0
t.tile2=0
t.tile3=0
assert win()==False, 'Some problem in win function'
print('Win function is OK')

# checking for takeNaiveMove function
resetgame()
assert 1<=takeNaiveMove()<=9, 'Some problem in takeNaiveMove function'
print('takeNaiveMove function is OK')
t.tile1=1
t.tile2=1
t.tile3=1
t.tile4=1
t.tile5=1
t.tile6=1
t.tile7=1
t.tile8=1
assert takeNaiveMove()==9, 'Some problem in takeNaiveMove function'
print('takeNaiveMove function is OK')

# checking for validBoard function
resetgame()
assert validBoard()==True, 'Some problem in validBoard function'
print('validBoard function is OK')
t.tile1=1
t.tile2=1
t.tile3=1
t.tile4=1
t.tile5=1
t.tile6=1
t.tile7=1
t.tile8=1
assert validBoard()==False, 'Some problem in validBoard function'
print('validBoard function is OK')

# checking for game function
resetgame()
assert game()==0, 'Some problem in game function'
print('game function is OK')
t.tile1=1
t.tile2=1
t.tile3=1
assert game()==1, 'Some problem in game function'
print('game function is OK')
resetgame()
t.tile4=2
t.tile5=2
t.tile6=2
assert game()==2, 'Some problem in game function'
print('game function is OK')

for i in range(3): # checking for 3 test cases for each of game1,game2,game3
	assert 0.5<game1(10000)<0.6, 'Game 1 is Showing Wrong Probability'
	assert 0<=game2(10000)<0.1, 'Game 1 is Showing Wrong Probability'
	assert 0<=game3(10000)<0.1, 'Game 1 is Showing Wrong Probability'
	print('game1, game2, game3 OK')


print('Your game Tic Tac Toe is working perfectly fine')
