#!/usr/bin/env python

#python code for raspberry pi

#import serial
#import RPi.GPIO as GPIO
#import time

#ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
#ser.baudrate=9600
#def blink(pin):

#GPIO.output(pin,GPIO.HIGH) 
#------------------------------------------------------------------------------------------------------------

# Name: ship#()
# Description: This function calculates the best location to place each ship
# Input: ProbMatrix - overall prob matrix for ai side of the board
# Output: Matrix - contains locations of the ships
def placeShips(aiMatrix):

	aiMatrixCopy = aiMatrix[:]

	aiMatrixCopy = ship2(aiMatrixCopy) #ship of length 2

	aiMatrixCopy = ship3(aiMatrixCopy) #first ship of length 3

	aiMatrixCopy = ship3(aiMatrixCopy) #second ship of length 3

	aiMatrixCopy = ship4(aiMatrixCopy) #ship of length 4

	aiMatrixCopy = ship5(aiMatrixCopy) #ship of length 5

	return aiMatrixCopy

# Name: ship#()
# Description: This function calculates the best location to place each ship by
# looking at every possible ship placement and using probability superposition
# to select the orientation with the smallest probability of being guessed
# Input: ProbMatrix - overall prob matrix for ai side of the board
# Output: Matrix - contains locations of the ships

def ship2(matrix):
	#loop through the AI boards history matrix (the human user guesses) aka aiMatrix

	one = 1.0
	two = 1.0
	rows, columns = 10, 10
	minProb = 1
	p1x = 0 #the row of the first position
	p1y = 0 #the column of the fist position
	p2x = 0 #the row of the second position
	p2y = 0 #the column of the second position

	#horizontal checking for ship of size 2
	for i in range(rows):
		for j in range(9):
			one = matrix[i][j]
			two = matrix[i][j+1]

			#we now get the joint probability
			prob = one*two
			if prob < minProb:
				minProb = prob
				p1x, p2x = i, i
				p1y = j
				p2y = j+1

	#vertical checking for ship of size 2
	for i in range(columns):
		for j in range(9):
			one = matrix[j][i]
			two = matrix[j+1][i]

			#we now get the joint probability
			prob = one*two
			if prob < minProb:
				minProb = prob
				p1x = j
				p1y, p2y = i, i
				p2x = j+1

	#now to make sure that no positions are chosen for multiple ships, we set those probabilities to values greater than 1 so they never get chosen
	# but also the value is 2 so we know which positions are for the ship of size 2
	matrix[p1x][p1y] = 2
	matrix[p2x][p2y] = 2

	#we can either all the positions or just one position 
	return (matrix)

def ship3(matrix):
	#loop through the AI boards history matrix (the human user guesses) aka aiMatrix

	fone = 1.0
	two = 1.0
	three = 1.0
	rows, columns = 10, 10
	minProb = 1
	p1x = 0 #the row of the first position
	p1y = 0 #the column of the fist position
	p2x = 0 #the row of the second position
	p2y = 0 #the column of the second position
	p3x = 0 #the row of the third position
	p3y = 0 #the column of the third position

	#horizontal checking for ship of size 3
	for i in range(rows):
		for j in range(8):
			one = matrix[i][j]
			two = matrix[i][j+1]
			three = matrix[i][j+2]

			#we now get the joint probability
			prob = one*two*three
			if prob < minProb:
				minProb = prob
				p1x, p2x, p3x = i, i, i
				p1y = j
				p2y = j+1
				p3y = j+2

	#vertical checking for ship of size 3
	for i in range(columns):
		for j in range(8):
			one = matrix[j][i]
			two = matrix[j+1][i]
			three = matrix[j+2][i]

			#we now get the joint probability
			prob = one*two*three
			if prob < minProb:
				minProb = prob
				p1x = j
				p1y, p2y, p3y = i, i, i
				p2x = j+1
				p3x = j+2

	#now to make sure that no positions are chosen for multiple ships, we set those probabilities to values greater than 1 so they never get chosen
	# but also the value is 3 so we know which positions are for the ship of size 3
	matrix[p1x][p1y] = 3
	matrix[p2x][p2y] = 3
	matrix[p3x][p3y] = 3

	#we can either all the positions or just one position 
	return (matrix)

def ship4(matrix):
	#loop through the AI boards history matrix (the human user guesses) aka aiMatrix

	one = 1.0
	two = 1.0
	three = 1.0
	four = 1.0
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
	for i in range(rows):
		for j in range(7):
			one = matrix[i][j]
			two = matrix[i][j+1]
			three = matrix[i][j+2]
			four = matrix[i][j+3]

			#we now get the joint probability
			prob = one*two*three*four
			if prob < minProb:
				minProb = prob
				p1x, p2x, p3x, p4x = i, i, i, i
				p1y = j
				p2y = j+1
				p3y = j+2
				p4y = j+3

	#vertical checking for ship of size 4
	for i in range(columns):
		for j in range(7):
			one = matrix[j][i]
			two = matrix[j+1][i]
			three = matrix[j+2][i]
			four = matrix[j+3][i]

			#we now get the joint probability
			prob = one*two*three*four
			if prob < minProb:
				minProb = prob
				p1x = j
				p1y, p2y, p3y, p4y = i, i, i, i
				p2x = j+1
				p3x = j+2
				p4x = j+3

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

	one = 1.0
	two = 1.0
	three = 1.0
	four = 1.0
	five = 1.0
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
	for i in range(rows):
		for j in range(6):
			one = matrix[i][j]
			two = matrix[i][j+1]
			three = matrix[i][j+2]
			four = matrix[i][j+3]
			five = matrix[i][j+4]

			#we now get the joint probability
			prob = one*two
			if prob < minProb:
				minProb = prob
				p1x, p2x, p3x, p4x, p5x = i, i, i, i, i
				p1y = j
				p2y = j+1
				p3y = j+2
				p4y = j+3
				p5y = j+4

	#vertical checking for ship of size 5
	for i in range(columns):
		for j in range(6):
			one = matrix[j][i]
			two = matrix[j+1][i]
			three = matrix[j+2][i]
			four = matrix[j+3][i]
			five = matrix[j+4][i]

			#we now get the joint probability
			prob = one*two
			if prob < minProb:
				minProb = prob
				p1x = j
				p1y, p2y, p3y, p4y, p5y = i, i, i, i, i
				p2x = j+1
				p3x = j+2
				p4x = j+3
				p5x = j+4


	#now to make sure that no positions are chosen for multiple ships, we set those probabilities to values greater than 1 so they never get chosen
	# but also the value is 5 so we know which positions are for the ship of size 5
	matrix[p1x][p1y] = 5
	matrix[p2x][p2y] = 5
	matrix[p3x][p3y] = 5
	matrix[p4x][p4y] = 5
	matrix[p4x][p5y] = 5

	#we can either all the positions or just one position 
	return (matrix)


# Name: updateBoard()
# Description: In this function, we update the gameMatrix with every move so
# that it is accurate for the next turn
# Input: X/Row location, Y/Column location, ProbMatrix(overall prob matrix for
# human/ai), GameMatrix(current game matrix for human/ai)
# Output: True if ship was hit, False if missed, Ship Size if hit
def updateBoard(x, y, probMatrix, gameMatrix):
	
	row = x
	col = y

	# HIT
	if gameMatrix[row][col] > 1 : #if there is a ship in that position

		shipSize = gameMatrix[row][col]
		prob = probMatrix[row][col]
		distProb = prob/99 #need to evenly distribute that probably to the rest of the board
		for i in range(10):
			for j in range(10): #because 10x10 board size
				gameMatrix[i][j] = gameMatrix[i][j] + distProb
		gameMatrix[row][col] = 0 #set probably of that position in current game to be zero
		
		# updates ai side probability board
		hitProb = 0.0004032258/gamesPlayed
		posProb = hitProb/99 #because there are 99 other positions
		probMatrix[row][col] = probMatrix[row][col] + hitProb + posProb #adding posProb because it will be decremented in the loop
		for i in range(10):
			for j in range(10): #because 10x10 board size
				probMatrix[i][j] = probMatrix[i][j] - posProb

		return (True, shipSize) #return hit and size of ship if hit

	# MISS
	elif gameMatrix[row][col] < 1: #if there is no ship in that position

		# updates current game board
		prob = gameMatrix[row][col]
		distProb = prob/99 #need to evenly distribute that probably to the rest of the board
		for i in range(10):
			for j in range(10): #because 10x10 board size
				gameMatrix[i][j] = gameMatrix[i][j] + distProb
		gameMatrix[row][col] = 0 #set probably of that position in current game to be zero

		# updates ai side probability board
		probability = 0.0004032258
		newProbVal = probability/99 #because there are 99 other positions
		probMatrix[row][col] = probMatrix[row][col] - probability - newProbVal #decrementing newProbVal beause it will be added in the loop
		for i in range(10):
			for j in range(10): #because 10x10 board size
				probMatrix[i][j] = probMatrix[i][j] + newProbVal

		return False #return miss		


# Name: aiMove()
# Description: In this function, the AI determines where to target its next hit
# by finding position with highest probability
# Input: None
# Output: Target locations (x/row, y/col)
def aiMove():

	#determine position to hit
	#update human side probability boards
	#update human current game board
	#update LED board


	# determine position to hit by finding largest probability in human side board
	maxValue = 0
	row, col = 0, 0 #the row and column positions
	for i in range(10):
		for j in range(10): #because 10x10 matrix
			if gameHumanMatrix[i][j] > maxValue:
				maxValue = gameHumanMatrix[i][j]
				row = i
				col = j

	return (row, col)


# Name: getShipOrientation()
# Description: In this function, the AI determines where to hit if a ship has 
# been hit (which orientation)
# Input: X - row of last hit
#		Y - column of last hit
#		Orientation - says if orientation of ship has been found
# Output: Next target locations (x/row, y/col), Orientation of ship (NESW)
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
# Description: In this function, the AI determines where to hit if a ship has
# been hit and we have determined the orientation
# Input: X - row of last hit
#		Y - column of last hit
#		Orientation - which direction we think the ship is facing
#		ogX - row of original X hit
#		ogY - column of original Y hit
# Output: Next target locations (x/row, y/col), nextOrientation (switch in case 
# we reach end of board)
def hitShip(x,y, orientation, ogX, ogY):

	nextX = 0
	nextY = 0
	nextOrientation = orientation

	if orientation == "north":
		if x > 1: #bounds checking
			nextX = x-1
			nextY = y
		else: #switch orientation
			nextOrientation = "south"
			nextX = ogX+1
			nextY = ogY

	elif orientation == "east":
		if y < 10: #bounds checking
			nextX = x
			nextY = y+1
		else:
			nextOrientation = "west"
			nextX = ogX
			nextY = ogY-1
		
	elif orientation == "south":
		if x < 10: #bounds checking
			nextX = x+1
			nextY = y
		else:
			nextOrientation = "north"
			nextX = ogX-1
			nextY = ogY

	elif orientation == "west":
		if y > 1: #bounds checking
			nextX = x
			nextY = y-1
		else:
			nextOrientation = "east"
			nextX = ogX
			nextY = ogY+1

	return (nextX, nextY, nextOrientation)


# Name: didShipSink()
# Description: In this function, we check whether or not the ship containing
# this point has sunk
# Input: X - row point in ship
#		Y - column point in ship
#		Orientation - the direction of the ship
#		GameMatrix - the matrix containing current board data
#		ShipSize = ship size so we know which values to look for in matrix
# Output: True if ship has sunk, False if ship has not sunk
def didShipSink(x, y, orientation, gameMatrix, shipSize):

	shipLength = shipSize

	if orientation == "north" or orientation == "south":
		for row in range(10):
			if gameMatrix[row][y] == shipLength:
				return False

	elif orientation == "west" or orientation == "east":
		for col in range(10):
			if gameMatrix[x][col] == shipLength:
				return False

	# maybe do this by checking ship size and checking how many hits there have been and seeing if they have all been on the same size shio
	# edge case is two of the 3 length boats adjacent, sooo we have to make sure that the other end of the orientation doesnt have a boat there too
	# possible fix - give one of the 3size boats a ship size of 3.5 or some other value

	return True





#------------------------------------------------------------------------------------------------------------

#at the start of the game the AI needs to place ships at the locations with the least probability
#do this using probability: algorithm is to look at every possible ship placement and put the ship at the place with the lowest joint probability


# These are the board we need throughout the game
# we will have a file that we will read at the start of every game and write to at the end of every game
# it will contain the boards that nee to be saves for every game
# one file for human player board
# one file for AI board

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

#this is the human side of the board... used during the duration of the game
gameHumanMatrix = humanMatrix[:]

#this is the ai side of the board... only used during the duration of the game
gameAiMatrix = aiMatrix[:]

#this will be a global variable that gets overwritten with the start of each new
#game and gets incremented at the end of each game.
gamesPlayed = 1;

#------------------------------------------------------------------------------------------------------------


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
shipSunk = False
ogX, ogY = None, None

#probably need to loop this

#Human gets to go first

while gameOver == False:
	# Human turn
	# TODO - get human input for target positions
	#x1, y1 = ...
	x1, y1 = 1, 1
	
	#updates boards and returns true if hit, false if miss
	hit1 = updateBoard(x1, y1, aiMatrix, gameAiMatrix) 
	
	# TODO - send hit/miss output to human player and let them know if ship has sunk
	# TODO - update LED boards based off of hit/miss

	# AI Turn
	if shipHit == False: #if no ship has been hit, look for regular target
		x2, y2 = aiMove()
		ogX, ogY = x2, y2
		hit2, length1 = updateBoard(x2, y2, humanMatrix, gameHumanMatrix)
		shipHit = hit2

	elif shipHit == True:

		if orientationKnown == False:
			x2, y2, orientation = getShipOrientation(x2, y2, direction)
			orientationKnown = True;
			hit2, length2 = updateBoard(x2, y2, humanMatrix, gameHumanMatrix)


	# need to save original hit in case we need to switch orientation

		elif orientationKnown == True:
			if hit2 == True and shipSunk == False:
				x2, y2, orientation = hitShip(x2, y2, orientation, ogX, ogY)

			elif hit2 == False: #if not sunk and miss
				x2, y2, orientation = getShipOrientation(x2, y2, direction)


	gameOver = True

	# TODO - send hit/miss output to human player
	# TODO - update LED boards based off of hit/miss






gamesPlayed = gamesPlayed + 1; 

# TODO - code to setup matrices for next game... update aiMatrix and humanMatrix for the start of the next game

