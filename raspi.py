#python code for raspberry pi

#we will have a file that we will read at the start of every game and write to at the end of every game
#it will contain the boards that nee to be saves for every game
#one file for human player board
#one file for AI board

import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
def blink(pin):


GPIO.output(pin,GPIO.HIGH) 

#------------------------------------------------------------------------------------------------------------

# These are the board we need throughout the game

#this only counts for the first game ever
startMatrix = [ [0.004032258, 0.006048387, 0.0076612902, 0.0084677418, 0.0088709676, 0.0088709676, 0.0084677418, 0.0076612902, 0.006048387, 0.004032258],
				[0.006048387, 0.008064516, 0.0096774192, 0.0104838708, 0.0108870966, 0.0108870966, 0.0104838708, 0.0096774192, 0.008064516, 0.006048387],
				[0.0076612902, 0.0096774192, 0.0112903224, 0.012096774, 0.0124999998, 0.0124999998, 0.012096774, 0.0112903224, 0.0096774192, 0.0076612902],
				[0.0084677418, 0.0104838708, 0.012096774, 0.0129032256, 0.0133064514, 0.0133064514, 0.0129032256, 0.012096774, 0.0104838708, 0.0084677418],
				[0.0088709676, 0.0108870966, 0.0124999998, 0.0133064514, 0.0137096772, 0.0137096772, 0.0133064514, 0.0124999998, 0.0108870966, 0.0088709676],
				[0.0088709676, 0.0108870966, 0.0124999998, 0.0133064514, 0.0137096772, 0.0137096772, 0.0133064514, 0.0124999998, 0.0108870966, 0.0088709676],
				[0.0084677418, 0.0104838708, 0.012096774, 0.0129032256, 0.0133064514, 0.0133064514, 0.0129032256, 0.012096774, 0.0104838708, 0.0084677418],
				[0.0076612902, 0.0096774192, 0.0112903224, 0.012096774, 0.0124999998, 0.0124999998, 0.012096774, 0.0112903224, 0.0096774192, 0.0076612902],
				[0.006048387, 0.008064516, 0.0096774192, 0.0104838708, 0.0108870966, 0.0108870966, 0.0104838708, 0.0096774192, 0.008064516, 0.006048387],
				[0.004032258, 0.006048387, 0.0076612902, 0.0084677418, 0.0088709676, 0.0088709676, 0.0084677418, 0.0076612902, 0.006048387, 0.004032258] ]

#this is the matrix of the human side that will get saved at the end of the game to be used at the start of the next game
endHumanMatrix = []

#this is the matrix of the ai side that will get saved at the end of the game to be used at the start of the next game
endAiMatrix = []

#TODO - the values in these matrices need to be changes for every game... read from file

#this is the board probability of the current game... starts the same as the startMatrix
#this is the humans side of the board... this gets saved at the end of the game to be used at the start of the next game
humanMatrix = [ [0.004032258, 0.006048387, 0.0076612902, 0.0084677418, 0.0088709676, 0.0088709676, 0.0084677418, 0.0076612902, 0.006048387, 0.004032258],
				[0.006048387, 0.008064516, 0.0096774192, 0.0104838708, 0.0108870966, 0.0108870966, 0.0104838708, 0.0096774192, 0.008064516, 0.006048387],
				[0.0076612902, 0.0096774192, 0.0112903224, 0.012096774, 0.0124999998, 0.0124999998, 0.012096774, 0.0112903224, 0.0096774192, 0.0076612902],
				[0.0084677418, 0.0104838708, 0.012096774, 0.0129032256, 0.0133064514, 0.0133064514, 0.0129032256, 0.012096774, 0.0104838708, 0.0084677418],
				[0.0088709676, 0.0108870966, 0.0124999998, 0.0133064514, 0.0137096772, 0.0137096772, 0.0133064514, 0.0124999998, 0.0108870966, 0.0088709676],
				[0.0088709676, 0.0108870966, 0.0124999998, 0.0133064514, 0.0137096772, 0.0137096772, 0.0133064514, 0.0124999998, 0.0108870966, 0.0088709676],
				[0.0084677418, 0.0104838708, 0.012096774, 0.0129032256, 0.0133064514, 0.0133064514, 0.0129032256, 0.012096774, 0.0104838708, 0.0084677418],
				[0.0076612902, 0.0096774192, 0.0112903224, 0.012096774, 0.0124999998, 0.0124999998, 0.012096774, 0.0112903224, 0.0096774192, 0.0076612902],
				[0.006048387, 0.008064516, 0.0096774192, 0.0104838708, 0.0108870966, 0.0108870966, 0.0104838708, 0.0096774192, 0.008064516, 0.006048387],
				[0.004032258, 0.006048387, 0.0076612902, 0.0084677418, 0.0088709676, 0.0088709676, 0.0084677418, 0.0076612902, 0.006048387, 0.004032258] ]
#humanMatrix = matrix read from file

#this is the ai side of the board... this gets saved at the end of the game to be used at the start of the next game
aiMatrix = [ [0.004032258, 0.006048387, 0.0076612902, 0.0084677418, 0.0088709676, 0.0088709676, 0.0084677418, 0.0076612902, 0.006048387, 0.004032258],
				[0.006048387, 0.008064516, 0.0096774192, 0.0104838708, 0.0108870966, 0.0108870966, 0.0104838708, 0.0096774192, 0.008064516, 0.006048387],
				[0.0076612902, 0.0096774192, 0.0112903224, 0.012096774, 0.0124999998, 0.0124999998, 0.012096774, 0.0112903224, 0.0096774192, 0.0076612902],
				[0.0084677418, 0.0104838708, 0.012096774, 0.0129032256, 0.0133064514, 0.0133064514, 0.0129032256, 0.012096774, 0.0104838708, 0.0084677418],
				[0.0088709676, 0.0108870966, 0.0124999998, 0.0133064514, 0.0137096772, 0.0137096772, 0.0133064514, 0.0124999998, 0.0108870966, 0.0088709676],
				[0.0088709676, 0.0108870966, 0.0124999998, 0.0133064514, 0.0137096772, 0.0137096772, 0.0133064514, 0.0124999998, 0.0108870966, 0.0088709676],
				[0.0084677418, 0.0104838708, 0.012096774, 0.0129032256, 0.0133064514, 0.0133064514, 0.0129032256, 0.012096774, 0.0104838708, 0.0084677418],
				[0.0076612902, 0.0096774192, 0.0112903224, 0.012096774, 0.0124999998, 0.0124999998, 0.012096774, 0.0112903224, 0.0096774192, 0.0076612902],
				[0.006048387, 0.008064516, 0.0096774192, 0.0104838708, 0.0108870966, 0.0108870966, 0.0104838708, 0.0096774192, 0.008064516, 0.006048387],
				[0.004032258, 0.006048387, 0.0076612902, 0.0084677418, 0.0088709676, 0.0088709676, 0.0084677418, 0.0076612902, 0.006048387, 0.004032258] ]
#aiMatrix = matrix read from file

#this is the human side of the board... only used during the duration of the game
gameHumanMatrix = humanMatrix[:]

#this is the ai side of the board... only used during the duration of the game
gameAiMatrix = aiMatrix[:]

gamesPlayed = 1; #this will be a global variable that gets overwritten with the start of each new game and gets incremented at the end of each game.

#------------------------------------------------------------------------------------------------------------


#at the start of the game the AI needs to place ships at the locations with the least probability
#do this using probability: algorithm is to look at every possible ship placement and put the ship at the place with the lowest joint probability
def placeShips(aiMatrix):

	aiMatrixCopy = aiMatrix[:]

	aiMatrixCopy = ship2(aiMatrixCopy) #ship of length 2

	aiMatrixCopy = ship3(aiMatrixCopy) #first ship of length 3

	aiMatrixCopy = ship3(aiMatrixCopy) #second ship of length 3

	aiMatrixCopy = ship4(aiMatrixCopy) #ship of length 4

	aiMatrixCopy = ship5(aiMatrixCopy) #ship of length 5

	return aiMatrixCopy

#these functions do the probability calculations for each ship placement

def ship2(matrix):
	#loop through the AI boards history matrix (the human user guesses) aka aiMatrix

	float one = 1
	float two = 1
	rows, columns = 10, 10
	minProb = 1
	p1x = 0 #the row of the first position
	p1y = 0 #the column of the fist position
	p2x = 0 #the row of the second position
	p2y = 0 #the column of the second position

	#horizontal checking for ship of size 2
	for i in range(row):
		for x in range(10) and y in range(9)
			one = matrix[i][x]
			two = matrix[i][1+y]

			#we now get the joint probability
			prob = one*two
			if prob < minProb:
				minProb = prob
				p1x, p2x = i, i
				p1y = x
				p2y = 1+y

	#vertical checking for ship of size 2
	for i in range(column):
		for x in range(10) and y in range(9)
			one = matrix[x][i]
			two = matrix[1+y][i]

			#we now get the joint probability
			prob = one*two
			if prob < minProb:
				minProb = prob
				p1x = x
				p1y, p2y = i, i
				p2x = 1+y

	#now to make sure that no positions are chosen for multiple ships, we set those probabilities to values greater than 1 so they never get chosen
	# but also the value is 2 so we know which positions are for the ship of size 2
	matrix[p1x][p1y] = 2
	matrix[p2x][p2y] = 2

	#we can either all the positions or just one position 
	return (matrix)

def ship3(matrix):
	#loop through the AI boards history matrix (the human user guesses) aka aiMatrix

	float one = 1
	float two = 1
	float three = 1
	rows, columns = 10, 10
	minProb = 1
	p1x = 0 #the row of the first position
	p1y = 0 #the column of the fist position
	p2x = 0 #the row of the second position
	p2y = 0 #the column of the second position
	p3x = 0 #the row of the third position
	p3y = 0 #the column of the third position

	#horizontal checking for ship of size 3
	for i in range(row):
		for x in range(10) and y in range(8)
			one = matrix[i][x]
			two = matrix[i][1+y]
			three = matrix[i][2+y]

			#we now get the joint probability
			prob = one*two*three
			if prob < minProb:
				minProb = prob
				p1x, p2x, p3x = i, i, i
				p1y = x
				p2y = 1+y
				p3y = 2+y

	#vertical checking for ship of size 3
	for i in range(column):
		for x in range(10) and y in range(8)
			one = matrix[x][i]
			two = matrix[1+y][i]
			three = matrix[2+y][i]

			#we now get the joint probability
			prob = one*two*three
			if prob < minProb:
				minProb = prob
				p1x = x
				p1y, p2y, p3y = i, i, i
				p2x = 1+y
				p3x = 2+y

	#now to make sure that no positions are chosen for multiple ships, we set those probabilities to values greater than 1 so they never get chosen
	# but also the value is 3 so we know which positions are for the ship of size 3
	matrix[p1x][p1y] = 3
	matrix[p2x][p2y] = 3
	matrix[p3x][p3y] = 3

	#we can either all the positions or just one position 
	return (matrix)

def ship4(matrix):
	#loop through the AI boards history matrix (the human user guesses) aka aiMatrix

	float one = 1
	float two = 1
	float three = 1
	float four = 1
	rows, columns = 10, 10
	minProb = 1
	p1x = 0 #the row of the first position
	p1y = 0 #the column of the fist position
	p2x = 0 #the row of the second position
	p2y = 0 #the column of the second position
	p3x = 0 #the row of the third position
	p3y = 0 #the column of the third position
	p4x = 0 #the row of the fourth position
	p4y = 0 #the column of the fourth position

	#horizontal checking for ship of size 4
	for i in range(row):
		for x in range(10) and y in range(7)
			one = matrix[i][x]
			two = matrix[i][1+y]
			three = matrix[i][2+y]
			four = matrix[i][3+y]

			#we now get the joint probability
			prob = one*two*three*four
			if prob < minProb:
				minProb = prob
				p1x, p2x, p3x, p4x = i, i, i, i
				p1y = x
				p2y = 1+y
				p3y = 2+y
				p4y = 3+y

	#vertical checking for ship of size 4
	for i in range(column):
		for x in range(10) and y in range(7)
			one = matrix[x][i]
			two = matrix[1+y][i]
			three = matrix[2+y][i]
			four = matrix[3+y][i]

			#we now get the joint probability
			prob = one*two*three*four
			if prob < minProb:
				minProb = prob
				p1x = x
				p1y, p2y, p3y, p4y = i, i, i, i
				p2x = 1+y
				p3x = 2+y
				p4x = 3+y

	#now to make sure that no positions are chosen for multiple ships, we set those probabilities to values greater than 1 so they never get chosen
	# but also the value is 4 so we know which positions are for the ship of size 4
	matrix[p1x][p1y] = 4
	matrix[p2x][p2y] = 4
	matrix[p3x][p3y] = 4
	matrix[p4x][p4y] = 4

	#we can either all the positions or just one position 
	return (matrix)

def ship5(matrix):
	#loop through the AI boards history matrix (the human user guesses) aka aiMatrix

	float one = 1
	float two = 1
	float three = 1
	float four = 1
	float five = 1
	rows, columns = 10, 10
	minProb = 1
	p1x = 0 #the row of the first position
	p1y = 0 #the column of the fist position
	p2x = 0 #the row of the second position
	p2y = 0 #the column of the second position
	p3x = 0 #the row of the third position
	p3y = 0 #the column of the third position
	p4x = 0 #the row of the fourth position
	p4y = 0 #the column of the fourth position
	p5x = 0 #the row of the fifth position
	p5y = 0 #the column of the fifth position

	#horizontal checking for ship of size 5
	for i in range(row):
		for x in range(10) and y in range(6)
			one = matrix[i][x]
			two = matrix[i][1+y]
			three = matrix[i][2+y]
			four = matrix[i][3+y]
			five = matrix[i][4+y]

			#we now get the joint probability
			prob = one*two
			if prob < minProb:
				minProb = prob
				p1x, p2x, p3x, p4x, p5x = i, i, i, i, i
				p1y = x
				p2y = 1+y
				p3y = 2+y
				p4y = 3+y
				p5y = 4+y

	#vertical checking for ship of size 5
	for i in range(column):
		for x in range(10) and y in range(6)
			one = matrix[x][i]
			two = matrix[1+y][i]
			three = matrix[2+y][i]
			four = matrix[3+y][i]
			five = matrix[4+y][i]

			#we now get the joint probability
			prob = one*two
			if prob < minProb:
				minProb = prob
				p1x = x
				p1y, p2y, p3y, p4y, p5y = i, i, i, i, i
				p2x = 1+y
				p3x = 2+y
				p4x = 3+y
				p5x = 4+y


	#now to make sure that no positions are chosen for multiple ships, we set those probabilities to values greater than 1 so they never get chosen
	# but also the value is 5 so we know which positions are for the ship of size 5
	matrix[p1x][p1y] = 5
	matrix[p2x][p2y] = 5
	matrix[p3x][p3y] = 5
	matrix[p4x][p4y] = 5
	matrix[p4x][p5y] = 5

	#we can either all the positions or just one position 
	return (matrix)


#reads the board files to start the game
def readBoards():

#writes the board files at the end of the game
def writeBoards():

# Name: updateBoard()
# Description: In this function, we update the gameMatrix with every move so that it is accurate for the next turn
# Input: X/Row location, Y/Column location, ProbMatrix(overall prob matrix for human/ai), GameMatrix(current game matrix for human/ai)
# Output: Target locations (x/row, y/col)
def updateBoard(x, y, probMatrix, gameMatrix):
	
	# HIT
	if gameMatrix[row][col] > 1 : #if there is a ship in that position

		# updates current game board
		prob = gameMatrix[row][col]
		distProb = prob/99 #need to evenly distribute that probably to the rest of the board
		for i in range(10)
			for j in range(10) #because 10x10 board size
				gameMatrix[i][j] = gameMatrix[i][j] + distProb
		gameMatrix[row][col] = 0 #set probably of that position in current game to be zero
		
		# updates ai side probability board
		hitProb = 0.0004032258/gamesPlayed
		posProb = hitProb/99 #because there are 99 other positions
		probMatrix[row][col] = probMatrix[row][col] + hitProb + posProb #adding posProb because it will be decremented in the loop
		for i in range(10)
			for j in range(10) #because 10x10 board size
				probMatrix[i][j] = probMatrix[i][j] - posProb

		return True #return hit

	# MISS
	else if gameMatrix[row][col] < 1: #if there is no ship in that position

		# updates current game board
		prob = gameMatrix[row][col]
		distProb = prob/99 #need to evenly distribute that probably to the rest of the board
		for i in range(10)
			for j in range(10) #because 10x10 board size
				gameMatrix[i][j] = gameMatrix[i][j] + distProb
		gameMatrix[row][col] = 0 #set probably of that position in current game to be zero

		# updates ai side probability board
		probability = 0.0004032258
		newProbVal = probability/99 #because there are 99 other positions
		probMatrix[row][col] = probMatrix[row][col] - probability - newProbVal #decrementing newProbVal beause it will be added in the loop
		or i in range(10)
			for j in range(10) #because 10x10 board size
				probMatrix[i][j] = probMatrix[i][j] + newProbVal

		return False #return miss



# matrices will either be global or passed into the functions

# this function takes in the inputs x(the row of the target) and y(the column of the target)
# this funciton should return whether it was a hit(true) or miss(false)
# def humanMove(x, y):

	row = x;
	col = y;

	#update ai side probability boards
	#update ai current game board
	#update LED board

	# HIT
	if aiMatrixCopy[row][col] > 1 : #if there is a ship in that position

		# updates current game board
		prob = gameAiMatrix[row][col]
		distProb = prob/99 #need to evenly distribute that probably to the rest of the board
		for i in range(10)
			for j in range(10) #because 10x10 board size
				gameAiMatrix[i][j] = gameAiMatrix[i][j] + distProb
		gameAiMatrix[row][col] = 0 #set probably of that position in current game to be zero
		
		# updates ai side probability board
		hitProb = 0.0004032258/gamesPlayed
		posProb = hitProb/99 #because there are 99 other positions
		aiMatrix[row][col] = aiMatrix[row][col] + hitProb + posProb #adding posProb because it will be decremented in the loop
		for i in range(10)
			for j in range(10) #because 10x10 board size
				aiMatrix[i][j] = aiMatrix[i][j] - posProb

		return True #return hit

	# MISS
	else if aiMatrixCopy[row][col] < 1: #if there is no ship in that position

		# updates current game board
		prob = gameAiMatrix[row][col]
		distProb = prob/99 #need to evenly distribute that probably to the rest of the board
		for i in range(10)
			for j in range(10) #because 10x10 board size
				gameAiMatrix[i][j] = gameAiMatrix[i][j] + distProb
		gameAiMatrix[row][col] = 0 #set probably of that position in current game to be zero

		# updates ai side probability board
		probability = 0.0004032258
		newProbVal = probability/99 #because there are 99 other positions
		aiMatrix[row][col] = aiMatrix[row][col] - probability - newProbVal #decrementing newProbVal beause it will be added in the loop
		or i in range(10)
			for j in range(10) #because 10x10 board size
				aiMatrix[i][j] = aiMatrix[i][j] + newProbVal

		return False #return miss
		

# Name: aiMove()
# Description: In this function, the AI determines where to target its next hit
# Input: Hit - if last AI move hit(true) or missed(false) a ship,
# Output: Target locations (x/row, y/col)
def aiMove(hit):

	#determine position to hit
	#update human side probability boards
	#update human current game board
	#update LED board


	# determine position to hit by finding largest probability in human side board
	maxValue = 0
	row, col = 0, 0 #the row and column positions
	for i in range(10)
		for j in range(10) #because 10x10 matrix
			if gameHumanMatrix[i][j] > maxValue
				maxValue = gameHumanMatrix[i][j]
				row = i
				col = j

	return (row, col)


	# HIT
	#if humanMatrix[row][col] > 1 : #if there is a ship in that position

		# # updates current game board
		# prob = gameHumanMatrix[row][col]
		# distProb = prob/99 #need to evenly distribute that probably to the rest of the board
		# for i in range(10)
		# 	for j in range(10) #because 10x10 board size
		# 		gameHumanMatrix[i][j] = gameHumanMatrix[i][j] + distProb
		# gameHumanMatrix[row][col] = 0 #set probably of that position in current game to be zero
		
		# # updates ai side probability board
		# hitProb = 0.0004032258/gamesPlayed
		# posProb = hitProb/99 #because there are 99 other positions
		# humanMatrix[row][col] = humanMatrix[row][col] + hitProb + posProb #adding posProb because it will be decremented in the loop
		# for i in range(10)
		# 	for j in range(10) #because 10x10 board size
		# 		humanMatrix[i][j] = humanMatrix[i][j] - posProb

		# return (True, row, col) #return hit

	# MISS
	#else if humanMatrix[row][col] < 1: #if there is no ship in that position

		# updates current game board
		# prob = gameHumanMatrix[row][col]
		# distProb = prob/99 #need to evenly distribute that probably to the rest of the board
		# for i in range(10)
		# 	for j in range(10) #because 10x10 board size
		# 		gameHumanMatrix[i][j] = gameHumanMatrix[i][j] + distProb
		# gameHumanMatrix[row][col] = 0 #set probably of that position in current game to be zero

		# # updates ai side probability board
		# probability = 0.0004032258
		# newProbVal = probability/99 #because there are 99 other positions
		# humanMatrix[row][col] = humanMatrix[row][col] - probability - newProbVal #decrementing newProbVal beause it will be added in the loop
		# or i in range(10)
		# 	for j in range(10) #because 10x10 board size
		# 		humanMatrix[i][j] = humanMatrix[i][j] + newProbVal

		# return (False, row, col) #return miss

# Name: getShipOrientation()
# Description: In this function, the AI determines where to hit if a ship has been hit (which orientation)
# Input: X - row of last hit
#		Y - column of last hit
#		Orientation - says if orientation of ship has been found
# Output: Next target locations (x/row, y/col), Orientation - of ship to hit (NESW)
def getShipOrientation(x,y):
	#check all orientations around the hit position to find which osurrounding position has the highest probability
	
	maxProb = 0
	nextX = 0
	nextY = 0
	orientation = None

	if x > 1: #bounds checking
		val = gameHumanMatrix[x-1][y] #north
		if val > maxProb:
			maxProb = val
			nextX = x-1
			nextY = y
			orientation = "north"

	if y < 10: #bounds checking
		val = gameHumanMatrix[x][y+1] #east
		if val > maxProb:
			maxProb = val
			nextX = x
			nextY = y+1
			orientation = "east"
	
	if x < 10: #bounds checking
		val = gameHumanMatrix[x+1][y] #south
		if val > maxProb:
			maxProb = val
			nextX = x+1
			nextY = y
			orientation = "south"

	if y > 1: #bounds checking
		val = gameHumanMatrix[x][y-1] #west
		if val > maxProb:
			maxProb = val
			nextX = x
			nextY = y-1
			orientation = "west"


	#return the next position to hit and direction (n, e, s, w)
	return (nextX, nextY, orientation)

# Name: hitShip()
# Description: In this function, the AI determines where to hit if a ship has been hit and we have determined the orientation
# Input: X - row of last hit
#		Y - column of last hit
#		Orientation - which direction we think the ship is facing
# Output: Next target locations (x/row, y/col), nextOrientation (switch in case we reach end of board)
def hitShip(x,y, orientation):

	nextX = 0
	nextY = 0
	nextOrientation = orientation

	if orientation == "north":
		if x > 1: #bounds checking
			nextX = x-1
			nextY = y
		else: #switch orientation
			nextOrientation = "south"

	else if orientation == "east":
		if y < 10: #bounds checking
			nextX = x
			nextY = y+1
		else:
			nextOrientation = "west"
		
	else if orientation == "south":
		if x < 10: #bounds checking
			nextX = x+1
			nextY = y
		else:
			nextOrientation = "north"

	else if orientation == "west":
		if y > 1: #bounds checking
			nextX = x
			nextY = y-1
		else:
			nextOrientation = "east"

	return (nextX, nextY, nextOrientation)



# START OF THE MAIN CODE

# pregame setup
gameOver = False #will be set to true when all ships have sunk and someone wins

gameAiMatrix = placeShips(aiMatrix) #place ships onto the gameAI Matrix
# TODO - get user input from buttons for user to place ships


hit2 = False #need hit2 to be outside loop so that it can be saved after every loop iteration...
x2, y2 = None, None
shipHit = False
orientationKnown = False
orientation = None
shipSunk == False

#probably need to loop this

#Human gets to go first

while gameOver == False:
	# Human turn
	# TODO - get human input for target positions
	#x1, y1 = ...
	hit1 = updateBoard(x1, y1, aiMatrix, gameAiMatrix) #updates boards and returns true if hit, false if miss
	# TODO - send hit/miss output to human player and let them know if ship has sunk
	# TODO - update LED boards based off of hit/miss

	# AI Turn
	if shipHit == False: #if no ship has been hit, look for regular target
		x2, y2 = aiMove(hit2, x2, y2)
		hit2 = updateBoard(x2, y2, humanMatrix, gameHumanMatrix)
		shipHit = hit2

	else if shipHit = True:

		if orientationKnown == False:
			x2, y2, orientation = getShipOrientation(x2, y2, direction)
			orientationKnown = True;
			hit2 = updateBoard(x2, y2, humanMatrix, gameHumanMatrix)


# need to save original hit in case we need to switch orientation

		else if orientationKnown == True:
			if hit2 == True and shipSunk == False:
				x2, y2, orientation = hitShip(x2, y2, orientation)

			else if hit2 == False: #if not sunk and miss, need to switch orientation by 180 degrees
				orientation = 



		













	if shipHit == False: #if no ship has been hit, look for regular target
		x2, y2 = aiMove(hit2, x2, y2)
		hit2 = updateBoard(x2, y2, humanMatrix, gameHumanMatrix)
		if hit2 == True:
			shipHit = True
	else if shipHit == True: #if ship has been hit
		x2, y2 = shipHit(x2, y2)
		hit2 = updateBoard(x2, y2, humanMatrix, gameHumanMatrix)
	else if shipHit == True and hit2 == False:

	else if shipSunk == True:




	# TODO - send hit/miss output to human player
	# TODO - update LED boards based off of hit/miss






gamesPlayed = gamesPlayed + 1; 

# TODO - code to setup matrices for next game... update aiMatrix and humanMatrix for the start of the next game








hit = humanMove(x,y) #x, y need to be gotten from arduino input
if hit == True #send user some feedback that says they got a hit and update led board to set x/y led light on board to light up

hit2, x1, y1 = aiMove()
#if hit2 == True update led board

hit = humanMove(x2,y2) #this could be wrong but its here for reference
#human user should do another turn and then on the ais next turn he can check if that last move was a hit and if so run the shiphit function

if hit2 == True: #hen ai needs to guess positions around it in order to sink the ship
	shipHit(x1,y1) #input the position where there was a hit

#we can redo this to have functions that detemine where to hit (for the ai) or take human input for where to hit
#and then another function to update the board no matter whos turn, we just input the board names


gamesPlayed = gamesPlayed + 1; 



# import sys

# def main(argv):
#     n = int(argv[1])
#     print(n + 1)

# if __name__ == '__main__':
#     sys.exit(main(sys.argv))