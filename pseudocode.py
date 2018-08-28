# --------------------- OBJECT ORIENTED PROGRAMMING ----------------------
class Ship:
	'Common base class for all ships'
	shipCount = 0

	def __init__():
		shipCount += 1
		#TODO		


# --------------------- FUNCTIONS THAT MAY BE USEFUL ----------------------
# These functions will still be helpful once you implement that AI
# But they may need to be updated later on
# You may also create ay additional functions you find useful


# Name: getHumanShipInput()
# Description: This function prompts the user to enter ship placements and
# places the ships in the human side matrix
# Input: Human Ship Matrix - contains locations of the humans ships
# Output: humanShips - the list of the humans ships
def getHumanShipInput(playerBottomMatrix):
	# TODO
	# Prompt user to enter ship locations
		# Check to see that ships are of size 2, 3, 3, 4, 5
		# Check to make sure ships are not overlapping
	# For each input, create Ship object
		# Place ship on the first players matrix in the correct locations
		# Place ship in a list that will contain all of this players ships
	# Return list of players ships

# Name: placeAiShips()
# Description: This function places the AIs ships on the matrix
# Input: AI Ship Matrix - contains locations of the AIs ships
# Output: aiShips - the list of AIs ships
def placeAiShips(aiBottomMatrix):
	# TODO
	# Loop through AI probability matrix to find smallest superpositions
	# for each ship.
		# Start by placing the smallest ship first, and work your way to placing
		# the largest ship
			# The reason for this that the smaller the ship, the harder it is to
			# hit because it has less possible locations. By giving the smaller
			# ship the least likely location, it makes it even harder to hit,
			# which will help the AI win.
		# Make sure ships are not overlapping
	# For each ship placement, create Ship object
		# Place ship on the AIs matrix in the correct locations
		# Place ship in a list that will contain all of this players ships
	# Return list of AIs ships


# Name: humanTurn()
# Description: This function prompts user to input their next target and 
# Input: playerTopMatrix - need to check that for previous moves
# Output: Target row/column
def humanTurn(humanTopMatrix):
	# TODO
	# Prompt user to enter target location
		# Check to see that location was not already targeted
	# Return inputted locations


# Name: aiTurn()
# Description: This function determines the AIs next target
# Input: humanProbMatrix - need to check that highest probability
# Output: Target row/column
def aiTurn(humanProbMatrix):
	# TODO
	# Loop through humans probability board
		# determine location with the highest probability
	# Return x/row and y/column of that location



# Name: updateBoard()
# Description: In this function, we update the playerTopMatrix with every move,
# and we update ship objects in shipMatrix to detect sinks in the future
# Input: X/Row location, Y/Column location, playerTopMatrix(matrix of players moves),
# 		otherPlayerBottomMatrix(other players matrix to check if ship is there)
# 		otherPlayerShips(contains opponents ships)
#		probMatrix - the probability matrix that needs to be updated
#			(humanProbMatrix if AIs turn, AiProbMatrix is humans turn)
# Output: True if ship was hit, False if missed
def updateBoard(x, y, playerTopMatrix, otherPlayerBottomMatrix, otherPlayerShips, probMatrix):
	# TODO
	# Check the other players bottom matrix if ship is there
		# Update playerTopMatrix accordingly
		# Update probability matrix accordingly
			# Update method detailed in documentation.
	# If ship was hit, update ship object with hit and/or hit location
		# Only if you choose to implement the game this way
	# Return hit(True) or miss(False)



# Name: isGameOver()
# Description: This function checks to see if the game is over. Called after
# each human or Ai turn
# Input: ship list - list containing the human/ai ships
# Output: True - game is over if all ships have been sunk
#         False - game is not over because not all ships have been sunk
def isGameOver(shipsList):
	# TODO
	# Loop through list of ships
		# if all ships have sunk, game is over


# ------------------------------ MAIN CODE -------------------------------

# TODO - Create 4 empty matrices for each players perspective. These will contain the ships.
	# humanBottomMatrix
	# humanTopMatrix
	# aiBottomMatrix
	# aiTopMatrix

# This is the matrix contianing the starting probabilities.
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

# TODO - for the first game, make four copies of his matrix.
	# Two keep track of the probability throughout the game to help decision making for the current game
	# Two keep track of the probability throught the game to help decision making for the next game
		# Directions to updated these matrices are in the documentation explaining the game setup.
	# aiProbMatrix - to keep track of the AI side - where to place ships based on human guesses
	# humanProbMatrix - One to keep track of the human side - where to target based on hits/misses
	# Both AI matrices and Human matrices are exactly the same at the start of the game.
	# Hint - use the deepcopy() function, otherwise one change will affect all 
	# the other matrices as well


# TODO - In any other game, you must read the updated matrix from a text file.
	# aiProbMatrix - to keep track of the AI side - where to place ships based on human guesses
	# humanProbMatrix - One to keep track of the human side - where to target based on hits/misses
	# Both AI matrices and Human matrices are exactly the same at the start of the game.
	# Hint - use the deepcopy() function, otherwise one change will affect all 
	# the other matrices as well


# First player places ships
humanShips = getHumanShipInput(humanBottomMatrix)

# Second player places ships
aiShips = placeAiShips(aiBottomMatrix)


while game is not over
	# Human players turn
	humanTurn(humanTopMatrix)
	hit1 = updateBoard()
	isGameOver(aiShips)

	# AI players turn
	aiTurn(humanProbMatrix)
	hit2 = updateBoard()
	isGameOver(humanShips)
