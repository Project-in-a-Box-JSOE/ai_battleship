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


#reads the board files to start the game
def readBoards():


#writes the board files at the end of the game
def writeBoards():


#updates temp board matrices with each move
def updateBoards():

#at the start of the game the AI needs to place ships at the locations with the least probability
#do this using probability: algorithm is to look at every possible ship placement and put the ship at the place with the lowest joint probability
def placeShips(aiMatrix):

	aiMatrixCopy = aiMatrix[:]

	aiMatrixCopy = ship2(aiMatrixCopy) #ship of length 2

	aiMatrixCopy = ship3(aiMatrixCopy) #first ship of length 3

	aiMatrixCopy = ship3(aiMatrixCopy) #second ship of length 3

	aiMatrixCopy = ship4(aiMatrixCopy) #ship of length 4

	aiMatrixCopy = ship5(aiMatrixCopy) #ship of length 5

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

endHumanMatrix = []
endAiMatrix = []

#this is the board probability of the current game... starts the same as the startMatrix
#this is the humans ship placement and the ai guesses impact this board
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

#this is the AIs side of the board, with the AI ship placement and the human guesses impact this board
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


#start by getting input from user on where they place ships

#then get the AI to place ships using the placeShips function
placeShips(aiMatrix)

#we let the human make the first move





# import sys

# def main(argv):
#     n = int(argv[1])
#     print(n + 1)

# if __name__ == '__main__':
#     sys.exit(main(sys.argv))