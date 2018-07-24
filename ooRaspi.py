#!/usr/bin/env python

import sys
from copy import copy, deepcopy

class Ship:
   'Common base class for all ships'
   shipCount = 0

   def __init__(self, length, sunk, orientation, locations):
      self.length = length
      #self.sunk = sunk
      self.orientation = orientation #might not even be necessary
      self.locations = locations #positions on board, list of list (X, y, hit)
      self.hits = 0
      Ship.shipCount += 1
      if self.length == self.hits:
         sunk = True
   
   def didShipSink(self):
      if self.length == self.hits:
         return True
      return False


# Name: ship#()
# Description: This function calculates the best location to place each ship.
# Input: ProbMatrix - overall prob matrix for ai side of the board
#        ShipMatrix - contains the locations of the ships
# Output: aiShips - list that contains all the AIs ships
def placeShips(gameAiMatrix, aiShipMatrix):

   aiShips = []

   ship2(gameAiMatrix, aiShipMatrix, aiShips) #ship of length 2

   ship3(gameAiMatrix, aiShipMatrix, aiShips) #first ship of length 3

   ship3(gameAiMatrix, aiShipMatrix, aiShips) #second ship of length 3

   ship4(gameAiMatrix, aiShipMatrix, aiShips) #ship of length 4

   ship5(gameAiMatrix, aiShipMatrix, aiShips) #ship of length 5

   return aiShips

# Name: ship#()
# Description: This function calculates the best location to place each ship by
# looking at every possible ship placement and using probability superposition
# to select the orientation with the smallest probability of being guessed.
# Then we create ship objects and place them in the ShipMatrix and ship list
# for later use
# Input: ProbMatrix - overall prob matrix for ai side of the board
#        ShipMatrix - contains the locations of the ships
#        AI Ships - list that contains all of the AIs ships
# Output: None

def ship2(matrix, shipMatrix, aiShips):
   #loop through the AI boards history matrix (the human user guesses) aka aiMatrix

   one = 1.0
   two = 1.0
   rows, columns = 10, 10
   minProb = 1
   p1x = 0 #the row of the first position
   p1y = 0 #the column of the fist position
   p2x = 0 #the row of the second position
   p2y = 0 #the column of the second position
   orientation = None

   #check horizontally and vertically for smallest superposition

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
            orientation = "horizontal"

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
            orientation = "vertical"


   # to make sure that no positions are chosen for multiple ships, we set those 
   # probabilities to values greater than 1 so they never get chosen
   # but also the value is 2 so we know which positions are for the ship of size 2
   matrix[p1x][p1y] = 2
   matrix[p2x][p2y] = 2

   #create ship and place it in the shipMatrix
   locations = [[p1x, p1y, False], [p2x, p2y, False]]
   ship = Ship(len(locations), False, orientation, locations)
   #for location in locations: #put ships in AI Ship Matrix
   #   shipMatrix[location[0]][location[1]] = [ship, 0]
   aiShips.append(ship)
   placeShipOnBoard(ship, aiShipMatrix)

def ship3(matrix, shipMatrix, aiShips):
   #loop through the AI boards history matrix (the human user guesses) aka aiMatrix

   one = 1.0
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
   orientation = None


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
            orientation = "horizontal"


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
            orientation = "vertical"


   #now to make sure that no positions are chosen for multiple ships, we set those probabilities to values greater than 1 so they never get chosen
   # but also the value is 3 so we know which positions are for the ship of size 3
   matrix[p1x][p1y] = 3
   matrix[p2x][p2y] = 3
   matrix[p3x][p3y] = 3

   #create ship and place it in the shipMatrix
   locations = [[p1x, p1y, False], [p2x, p2y, False], [p3x, p3y, False]]
   ship = Ship(len(locations), False, orientation, locations)
   #for location in locations: #put ships in AI Ship Matrix
   #   shipMatrix[location[0]][location[1]] = [ship, 0]
   aiShips.append(ship)
   placeShipOnBoard(ship, aiShipMatrix)

def ship4(matrix, shipMatrix, aiShips):
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
   orientation = None

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
            orientation = "horizontal"

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
            orientation = "vertical"

   #now to make sure that no positions are chosen for multiple ships, we set those probabilities to values greater than 1 so they never get chosen
   # but also the value is 4 so we know which positions are for the ship of size 4
   matrix[p1x][p1y] = 4
   matrix[p2x][p2y] = 4
   matrix[p3x][p3y] = 4
   matrix[p4x][p4y] = 4

   #create ship and place it in the shipMatrix
   locations = [[p1x, p1y, False], [p2x, p2y, False], [p3x, p3y, False], [p4x, p4y, False]]
   ship = Ship(len(locations), False, orientation, locations)
   #for location in locations: #put ships in AI Ship Matrix
   #   shipMatrix[location[0]][location[1]] = [ship, 0]
   aiShips.append(ship)
   placeShipOnBoard(ship, aiShipMatrix)

def ship5(matrix, shipMatrix, aiShips):
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
   orientation = None

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
            orientation = "horizontal"

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
            orientation = "vertical"


   #now to make sure that no positions are chosen for multiple ships, we set those probabilities to values greater than 1 so they never get chosen
   # but also the value is 5 so we know which positions are for the ship of size 5
   matrix[p1x][p1y] = 5
   matrix[p2x][p2y] = 5
   matrix[p3x][p3y] = 5
   matrix[p4x][p4y] = 5
   matrix[p5x][p5y] = 5

   #print(matrix)

   #create ship and place it in the shipMatrix
   locations = [[p1x, p1y, False], [p2x, p2y, False], [p3x, p3y, False], [p4x, p4y, False], [p5x, p5y, False]]
   ship = Ship(len(locations), False, orientation, locations)
   #for location in locations: #put ships in AI Ship Matrix
   #   shipMatrix[location[0]][location[1]] = [ship, 0]
   aiShips.append(ship)
   placeShipOnBoard(ship, aiShipMatrix)


# Name: updateBoard()
# Description: In this function, we update the gameMatrix with every move so
# that it is accurate for the next turn, we update the probablily matrix so it
# is valid for the next game, we update ship objects in shipMatrix to detect
# sinks in the future
# Input: X/Row location, Y/Column location, ProbMatrix(overall prob matrix for
# human/ai), GameMatrix(current game matrix for human/ai), ShipMatrix(contains
# human/ai ships)
# Output: True if ship was hit, False if missed
def updateBoards(x, y, probMatrix, gameMatrix, shipMatrix):
   
   row = x
   col = y

   #print(row, col)
   print(gameMatrix[row][col])
   #print(gameMatrix)

   # HIT
   if gameMatrix[row][col] > 1 : #if there is a ship in that position
   #if shipMatrix[row][col] != 0 : #if there is a ship in that position


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

      #update ship object
      #print(shipMatrix)
      #print(gameMatrix)
      #print(probMatrix)
      #print(shipMatrix[row][col][0])
      ship = shipMatrix[row][col][0]
      #print(ship)
      shipMatrix[row][col][1] = "X"
      #print(ship)
      ship.hits += 1
      for location in ship.locations: #setting that location as hit
         if location[0] == x and location[1] == y:
            location[2] = True

      return True #return hit

   # MISS
   elif gameMatrix[row][col] < 1: #if there is no ship in that position
   #elif shipMatrix[row][col] == 0: #if there is no ship in that position


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

      #if there was a miss, we do not need to update any ship objects, just the Matrix
      shipMatrix[row][col] = "O"


      return False #return miss     


# Name: aiMove()
# Description: In this function, the AI determines where to target its next hit
# by finding position with highest probability
# Input: None
# Output: Target locations (x/row, y/col)
def aiMove(gameHumanMatrix):

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


# Name: getShipDirection()
# Description: In this function, the AI determines where to hit if a ship has 
# been hit (which orientation)
# Input: X - row of last hit
#     Y - column of last hit
#     Orientation - says if orientation of ship has been found
# Output: Next target locations (x/row, y/col), Orientation of ship (NESW)
def getShipDirection(x,y):
   #check all orientations around the hit position to find which osurrounding position has the highest probability
   
   maxProb = 0
   nextX = 0
   nextY = 0
   direction = None

   if x > 0: #bounds checking
      val = gameHumanMatrix[x-1][y] #north
      if val > maxProb:
         maxProb = val
         nextX = x-1
         nextY = y
         direction = "north"

   if y < 9: #bounds checking
      val = gameHumanMatrix[x][y+1] #east
      if val > maxProb:
         maxProb = val
         nextX = x
         nextY = y+1
         direction = "east"
   
   if x < 9: #bounds checking
      val = gameHumanMatrix[x+1][y] #south
      if val > maxProb:
         maxProb = val
         nextX = x+1
         nextY = y
         direction = "south"

   if y > 0: #bounds checking
      val = gameHumanMatrix[x][y-1] #west
      if val > maxProb:
         maxProb = val
         nextX = x
         nextY = y-1
         direction = "west"


   #return the next position to hit and direction (n, e, s, w)
   return (nextX, nextY, direction)


# Name: switchOrientation()
# Description: In this function, we slip the direction if we reach the end of
# the board or if there is a hit followed by a miss
# Input: ogX - row of original X hit
#     ogY - column of original Y hit
#     Orientation - which direction we think the ship is facing
# Output: Next target locations (x/row, y/col), nextOrientation (switch in case 
# we reach end of board)
def switchOrientation(ogX, ogY, orientation):

   nextX = 0
   nextY = 0
   nextOrientation = orientation

   if orientation == "north":
      nextOrientation = "south"
      nextX = ogX+1
      nextY = ogY

   elif orientation == "east":
      nextOrientation = "west"
      nextX = ogX
      nextY = ogY-1

   elif orientation == "south":
         nextOrientation = "north"
         nextX = ogX-1
         nextY = ogY

   elif orientation == "west":
         nextOrientation = "east"
         nextX = ogX
         nextY = ogY+1

   return (nextX, nextY, nextOrientation)



# Name: hitShip()
# Description: In this function, the AI determines where to hit if a ship has
# been hit and we have determined the orientation
# Input: X - row of last hit
#     Y - column of last hit
#     Orientation - which direction we think the ship is facing
#     ogX - row of original X hit
#     ogY - column of original Y hit
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
         nextX, nextY, nextOrientation = switchOrientation(ogX, ogY, orientation)
         #nextOrientation = "south"
         #nextX = ogX+1
         #nextY = ogY

   elif orientation == "east":
      if y < 10: #bounds checking
         nextX = x
         nextY = y+1
      else:
         nextX, nextY, nextOrientation = switchOrientation(ogX, ogY, orientation)
         # nextOrientation = "west"
         # nextX = ogX
         # nextY = ogY-1
      
   elif orientation == "south":
      if x < 10: #bounds checking
         nextX = x+1
         nextY = y
      else:
         nextX, nextY, nextOrientation = switchOrientation(ogX, ogY, orientation)
         # nextOrientation = "north"
         # nextX = ogX-1
         # nextY = ogY

   elif orientation == "west":
      if y > 1: #bounds checking
         nextX = x
         nextY = y-1
      else:
         nextX, nextY, nextOrientation = switchOrientation(ogX, ogY, orientation)
         # nextOrientation = "east"
         # nextX = ogX
         # nextY = ogY+1

   return (nextX, nextY, nextOrientation)

# Name: highestProbDirection()
# Description: In this function, the AI determines direction to hit if a ship has
# been hit more than twice while trying to sink another ship
# Input: X - row of last hit
#     Y - column of last hit
#     Orientation - which direction we think the ship is facing
#     ogX - row of original X hit
#     ogY - column of original Y hit
# Output: Next target locations (x/row, y/col), nextOrientation (switch in case 
# we reach end of board)
#def highestProbDirection(ogX, ogY, x, y, probMatrix):

   # if ogX == x: #same row so horizontal

   #    #have to do bounds checking

   #    if ogY == 0: #then we just go off of y
   #       direction = 


   #    if ogY > y:
   #       smallerY = y
   #       biggerY = ogY
   #    else:
   #       smallerY = ogY
   #       biggerY = y
      
   #    prob1 = probMatrix[ogX][ogY]
   #    prob2 = probMatrix[ogX][y]


   # elif ogY == y: #same column so vertical



   # return direction


# Name: getHumanInput()
# Description: This function prompts the user to enter ship placements and
# places the ships in the human side matrix
# Input: Human Ship Matrix - contains locations of the ships
# Output: humanShips - the list of ships
def getHumanInput(gameHumanMatrix, humanShipMatrix):

   #humanShipMatrix = shipMatrix

   # TODO - figure out lighting up LEDs based on the user input

   print("For each ship, type the start location followed by ending location.")
   print("Type the row followed by a space followed by column.")
   print("Place a comma between each point of the ship.")
   print("Example: 2 3, 2 6")

   humanShips = []
   for i in range(2,6): #loop 5 times to do this for 5 ships
      
      string = "Please enter the start and end locations for ship of size " + str(i) + ".\n"
      # TODO - figure out how to prompt this with LEDS (maybe blinking ship of size ___ or just write number in LEDS)

      #print(string)
      var = input(string)
      var = var.replace(" ", "").replace(",", "")
      
      locations = [(int(var[0]), int(var[1]), False), (int(var[2]), int(var[3]), False)]
      #print("here1\n")
      orientation = getOrientation(locations) #check valid orientation
      #print(orientation)
      size = checkShipSize(orientation, locations) #check valid ship size
      #print("here3\n")
      overlap, locations = checkOverlap(orientation, size, locations, humanShipMatrix) #check is ship overlaps another
      #print("here4\n")
      #print (overlap)

      #if orientation or size not valid, reprompt user for locations
      while orientation == "none" or size != i or overlap == True:
         
         if orientation == "none":
            print("Sorry, you entered a ship that is not horizontal or vertical.")
            printHumanBoard(humanShipMatrix)
         elif size != i:
            print("Sorry, you entered a ship that is not of size ", i, ".")
            printHumanBoard(humanShipMatrix)
         elif overlap == True:
            print("Sorry, you entered a ship overlaps with another ship.")
            printHumanBoard(humanShipMatrix)

         var = input(string)
         var = var.replace(" ", "").replace(",", "")
         locations = [[int(var[0]), int(var[1]), False], [int(var[2]), int(var[3]), False]]
         orientation = getOrientation(locations)
         size = checkShipSize(orientation, locations)
         overlap, locations = checkOverlap(orientation, size, locations, humanShipMatrix)
         #print(overlap)


      #TODO - placing ship values on current board
      placeShipOnCurrentGameBoard(locations, gameHumanMatrix)
      ship = Ship(len(locations), False, orientation, locations)
      humanShips.append(ship)
      placeShipOnBoard(ship, humanShipMatrix)
      #print(humanShipMatrix)
      printHumanBoard(humanShipMatrix)
      #print(humanShipMatrix)

      if i == 3:
         string = "Please enter the start and end locations for the second ship of size " + str(i) + ".\n"
         var = input(string)
         var = var.replace(" ", "").replace(",", "")
         
         locations = [[int(var[0]), int(var[1]), False], [int(var[2]), int(var[3]), False]]
         orientation = getOrientation(locations) #check valid orientation
         size = checkShipSize(orientation, locations) #check valid ship size
         overlap, locations = checkOverlap(orientation, size, locations, humanShipMatrix) #check is ship overlaps another
         #print (overlap)

         #if orientation or size not valid, reprompt user for locations
         while orientation == "none" or size != i or overlap == True:
            
            if orientation == "none":
               print("Sorry, you entered a ship that is not horizontal or vertical.")
            elif size != i:
               print("Sorry, you entered a ship that is not of size ", i, ".")
            elif overlap == True:
               print("Sorry, you entered a ship overlaps with another ship.")
            
            var = input(string)
            var = var.replace(" ", "").replace(",", "")
            locations = [[int(var[0]), int(var[1]), False], [int(var[2]), int(var[3]), False]]
            orientation = getOrientation(locations)
            size = checkShipSize(orientation, locations)
            overlap, locations = checkOverlap(orientation, size, locations, humanShipMatrix)
            #print(overlap)

         placeShipOnCurrentGameBoard(locations, gameHumanMatrix)
         ship = Ship(len(locations), False, orientation, locations)
         humanShips.append(ship)
         placeShipOnBoard(ship, humanShipMatrix)
         printHumanBoard(humanShipMatrix)
         #print(humanShipMatrix)


   return humanShips


# Name: placeShipOnCurrentGameBoard()
# Description: This function places the ship length values in the current game
# board so that we can use the matrix throughout the game... used for human size
# Input: Locations - start and end location of the ship
#        GameMatrix - matrix containing values of current board
# Output: None
def placeShipOnCurrentGameBoard(locations, gameMatrix):
   lengthOfShip = len(locations)
   for i in range(lengthOfShip):
      x = locations[i][0]
      y = locations[i][1]
      gameMatrix[x][y] = lengthOfShip


# Name: getOrientation()
# Description: This function takes in the locations and gets orientation of ship
# Input: Locations list
# Output: Orientation (vertical/horizontal) or None (if user put invalid input)
def getOrientation(locations):
   if locations[0][0] == locations[1][0]: #if they have the same row
      return ("horizontal")
   elif locations[0][1] == locations[1][1]: #if they have the same column
      return ("vertical")
   else: #if the ship points are not in the same row or column
      return ("none")


# Name: checkShipSize()
# Description: This function checks to see if the user inputted points that
# match the ships size
# Input: Ship
# Output: length of ship, locations of ship
def checkShipSize(orientation, locations):

   length = 0
   #if orientation == "none" then length remains 0

   if orientation == "horizontal": #same row
      #we want to get the column calues
      val1 = locations[0][1]
      val2 = locations[1][1]
      length = abs(val1-val2) + 1

   elif orientation == "vertical": #same column
      #we want to get the row values
      val1 = locations[0][0]
      val2 = locations[1][0]
      length = abs(val1-val2) + 1

   return length


# Name: checkOverlap()
# Description: This function check if ship is overlapping another ship by finding
# all the points in between the start/end points and checking if there is a ship
# already at any of those points. This function also updates the locations list
# to include all of these points.
# Input: Orientation of ship, Length of ship, start/end locations of ship
# HumanShipMatrix - matrix that contains all of the humans ship in location
# Output: True if overlap, False otherwise
def checkOverlap(orientation, shipSize, locations, humanShipMatrix):

   #print(locations)
   newLocations = [] #list that will contain all the points of this ship

   if orientation == "none":
      return (False, locations)

   elif shipSize == 0:
      return (False, locations)

   elif orientation == "horizontal": #same row
      row = locations[0][0]
      startCol, endCol = 0, 0
      #print("in horizontal")

      #finding smaller column to make looping easier
      if locations[0][1] < locations[1][1]:
         startCol = locations[0][1]
         endCol = locations[1][1]
      else:
         startCol = locations[1][1]
         endCol = locations[0][1]

      for col in range(startCol, endCol+1):
         newLocations.append([row, col, False]) #append points to new list
         #print("HERE1")
         if humanShipMatrix[row][col] != 0: #if there is a ship there
            return (True, locations)

   elif orientation == "vertical": #same column
      column = locations[0][1]
      startRow, endRow = 0, 0
      #print("in vertical")

      #finding smaller row to make looping easier
      if locations[0][0] < locations[1][0]:
         startRow = locations[0][0]
         endRow = locations[1][0]
      else:
         startRow = locations[1][0]
         endRow = locations[0][0]

      #print(startRow, endRow)
      for row in range(startRow, endRow+1):
         newLocations.append([row, column, False]) #append points to new list
         #print("appended")
         if humanShipMatrix[row][column] != 0: #if there is a ship there
            #print("HERE2")
            return (True, locations)


   return (False, newLocations)


# Name: placeShipOnBoard()
# Description: This function takes in the ship and places it on the human matrix
# Input: Ship to place on Matrix
# Output: None
def placeShipOnBoard(ship, shipMatrix):

   for location in ship.locations:
      #print(location)
      row = location[0]
      column = location[1]
      shipMatrix[row][column] = [ship, 0] #placing ship in matrix
      #printBoards(humanShipMatrix, aiShipMatrix)


# TODO - replace this with update LED board?????
# Name: printHumanBoard()
# Description: This function takes in the shipMatrix and prints it out
# Input: Human Ship Matrix
# Output: None
def printHumanBoard(shipMatrix):

   print("Your Board:")
   tempShipMatrix = [[0 for x in range(10)] for y in range(10)] 

   for row in range(10):
      for column in range(10):

         if shipMatrix[row][column] == "O":
            tempShipMatrix[row][column] = "O"
         elif shipMatrix[row][column] != 0: #if there is a ship
            #print(shipMatrix[row][column])
            if shipMatrix[row][column][1] == "X": #if ship was hit
               tempShipMatrix[row][column] = "X"
            else:
               ship = shipMatrix[row][column][0]
               tempShipMatrix[row][column] = ship.length


      print(tempShipMatrix[row])
   print("\n")

   #print(tempShipMatrix)

# TODO - replace this with update LED board?????
# Name: printAiBoard()
# Description: This function takes in the shipMatrix and prints it out
# Input: Ai Ship Matrix
# Output: None
def printAiBoard(shipMatrix):
   
   print("Real AI Board:")
   tempShipMatrix = [[0 for x in range(10)] for y in range(10)] 

   for row in range(10):
      for column in range(10):

         if shipMatrix[row][column] == "O":
            tempShipMatrix[row][column] = "O"
         elif shipMatrix[row][column] != 0: #if there is a ship
               ship = shipMatrix[row][column][0]
               tempShipMatrix[row][column] = ship.length

      print(tempShipMatrix[row])
   print("\n")



   print("AI Board:")
   tempShipMatrix = [[0 for x in range(10)] for y in range(10)] 

   for row in range(10):
      for column in range(10):
         
         if shipMatrix[row][column] == "O":
            tempShipMatrix[row][column] = "O"

         elif shipMatrix[row][column] != 0: #if there is a ship there

            if shipMatrix[row][column][1] == "X": #if ship was hit
               tempShipMatrix[row][column] = "X"

         #else:
            #tempShipMatrix[row][column] = 0

      print(tempShipMatrix[row])
   print("\n")

   #print(tempShipMatrix)


# TODO - human turn - need this for testing before hardware implementation
# Name: humanTurn()
# Description: This function prompts user to input their next target
# Input: None
# Output: Target row/column
def humanTurn(aiShipMatrix):

   #print("Where would you like your next target to be?")
   print("YOUR TURN!")
   print("Type the row followed by a space followed by column. For example: 2 3")
   var = input("Where would you like your next target to be?\n")
   var = var.replace(" ", "")
   x, y = int(var[0]), int(var[1])

   print(aiShipMatrix[x][y])
   
   while aiShipMatrix[x][y] == "O": #then already hit here
      print("You have already target that location. Please select a different target.")
      var = input("Where would you like your next target to be?\n")
      var = var.replace(" ", "")
      x, y = int(var[0]), int(var[1])

   while aiShipMatrix[x][y] != "O" and aiShipMatrix[x][y] != 0 and aiShipMatrix[x][y][1] == "X": #then already hit here
      print("You have already target that location. Please select a different target.")
      var = input("Where would you like your next target to be?\n")
      var = var.replace(" ", "")
      x, y = int(var[0]), int(var[1])

   return (x, y)


# Name: isGameOver()
# Description: This function checks to see if the game is over. Called after
# each human or Ai turn
# Input: ship list - list containin the human/ai ships
# Output: True - game is over if all ships have been sunk
#         False - game is not over because not all ships have been sunk
def isGameOver(shipsList):

   for ship in shipsList:
      if ship.didShipSink() == False: #if there is a ship that has not been sunk
         #print(ship.length)
         return False

   return True



# -----------------------------------------------------------------------------

# Get number of games played (read from file)
# Gets incremented and saved at the end of each game

gamesPlayedFile = open("gamesPlayed.txt", "r")
gamesPlayed = int(gamesPlayedFile.read())
gamesPlayedFile.close()
#print(gamesPlayed)

# -----------------------------------------------------------------------------


#Matrix Initilizations

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

# Matrix files are as follows: each line in file contains value
# Order of values is the same as iterating through rows of matrix (left->right)
# and then to the next row

#if first game ever, start with starting matrix
#humanMatrix = startMatrix[:] #human side of probability board... used for duration of game
#aiMatrix = startMatrix[:] #ai side of probability board... used for duration of game
humanMatrix = deepcopy(startMatrix) #human side of probability board... used for duration of game
aiMatrix = deepcopy(startMatrix) #ai side of probability board... used for duration of game



if gamesPlayed > 1: #if not first game, read from files

   #do both at same time to be more efficient
   humanMatrixFile = open("humanMatrix.txt", "r")
   aiMatrixFile = open("aiMatrix.txt", "r")

   for i in range(100):
      for row in range(10):
         for column in range(10):
            #print(humanMatrixFile.readline())
            value1 = humanMatrixFile.readline()
            value2 = aiMatrixFile.readline()
            humanMatrix[row][column] = int(value1)
            aiMatrix[row][column] = int(value2)

   humanMatrixFile.close()
   aiMatrixFile.close()


#this is the board probability of the current game... starts the same as the startMatrix
#this is the humans side of the probability board... this gets saved at the end of the game to be used at the start of the next game
#humanMatrix = [ [0.004032258, 0.006048387, 0.0076612902, 0.0084677418, 0.0088709676, 0.0088709676, 0.0084677418, 0.0076612902, 0.006048387, 0.004032258],
            # [0.006048387, 0.008064516, 0.0096774192, 0.0104838708, 0.0108870966, 0.0108870966, 0.0104838708, 0.0096774192, 0.008064516, 0.006048387],
            # [0.0076612902, 0.0096774192, 0.0112903224, 0.012096774, 0.0124999998, 0.0124999998, 0.012096774, 0.0112903224, 0.0096774192, 0.0076612902],
            # [0.0084677418, 0.0104838708, 0.012096774, 0.0129032256, 0.0133064514, 0.0133064514, 0.0129032256, 0.012096774, 0.0104838708, 0.0084677418],
            # [0.0088709676, 0.0108870966, 0.0124999998, 0.0133064514, 0.0137096772, 0.0137096772, 0.0133064514, 0.0124999998, 0.0108870966, 0.0088709676],
            # [0.0088709676, 0.0108870966, 0.0124999998, 0.0133064514, 0.0137096772, 0.0137096772, 0.0133064514, 0.0124999998, 0.0108870966, 0.0088709676],
            # [0.0084677418, 0.0104838708, 0.012096774, 0.0129032256, 0.0133064514, 0.0133064514, 0.0129032256, 0.012096774, 0.0104838708, 0.0084677418],
            # [0.0076612902, 0.0096774192, 0.0112903224, 0.012096774, 0.0124999998, 0.0124999998, 0.012096774, 0.0112903224, 0.0096774192, 0.0076612902],
            # [0.006048387, 0.008064516, 0.0096774192, 0.0104838708, 0.0108870966, 0.0108870966, 0.0104838708, 0.0096774192, 0.008064516, 0.006048387],
            # [0.004032258, 0.006048387, 0.0076612902, 0.0084677418, 0.0088709676, 0.0088709676, 0.0084677418, 0.0076612902, 0.006048387, 0.004032258] ]
#humanMatrix = matrix read from file

#this is the ai side of the probability board... this gets saved at the end of the game to be used at the start of the next game
#aiMatrix = [ [0.004032258, 0.006048387, 0.0076612902, 0.0084677418, 0.0088709676, 0.0088709676, 0.0084677418, 0.0076612902, 0.006048387, 0.004032258],
            # [0.006048387, 0.008064516, 0.0096774192, 0.0104838708, 0.0108870966, 0.0108870966, 0.0104838708, 0.0096774192, 0.008064516, 0.006048387],
            # [0.0076612902, 0.0096774192, 0.0112903224, 0.012096774, 0.0124999998, 0.0124999998, 0.012096774, 0.0112903224, 0.0096774192, 0.0076612902],
            # [0.0084677418, 0.0104838708, 0.012096774, 0.0129032256, 0.0133064514, 0.0133064514, 0.0129032256, 0.012096774, 0.0104838708, 0.0084677418],
            # [0.0088709676, 0.0108870966, 0.0124999998, 0.0133064514, 0.0137096772, 0.0137096772, 0.0133064514, 0.0124999998, 0.0108870966, 0.0088709676],
            # [0.0088709676, 0.0108870966, 0.0124999998, 0.0133064514, 0.0137096772, 0.0137096772, 0.0133064514, 0.0124999998, 0.0108870966, 0.0088709676],
            # [0.0084677418, 0.0104838708, 0.012096774, 0.0129032256, 0.0133064514, 0.0133064514, 0.0129032256, 0.012096774, 0.0104838708, 0.0084677418],
            # [0.0076612902, 0.0096774192, 0.0112903224, 0.012096774, 0.0124999998, 0.0124999998, 0.012096774, 0.0112903224, 0.0096774192, 0.0076612902],
            # [0.006048387, 0.008064516, 0.0096774192, 0.0104838708, 0.0108870966, 0.0108870966, 0.0104838708, 0.0096774192, 0.008064516, 0.006048387],
            # [0.004032258, 0.006048387, 0.0076612902, 0.0084677418, 0.0088709676, 0.0088709676, 0.0084677418, 0.0076612902, 0.006048387, 0.004032258] ]
#aiMatrix = matrix read from file

#this is the human side of the board... used during the duration of the game
gameHumanMatrix = deepcopy(humanMatrix)
#human side of the board that shows where its ships are and keeps track of hits/misses
humanShipMatrix = [[0 for x in range(10)] for y in range(10)] 

#this is the ai side of the board... only used during the duration of the game
gameAiMatrix = deepcopy(aiMatrix)
#ai side of the board that shows where its ships are and keeps track of hits/misses
aiShipMatrix = [[0 for x in range(10)] for y in range(10)]

# -----------------------------------------------------------------------------

# START OF THE MAIN CODE

print("first print")
print("ai game matrix:")
print(gameAiMatrix)
print("\n")
print("human game matrix:")
print(gameHumanMatrix)
print("\n")



# pregame setup
gameOver = False #will be set to true when all ships have sunk and someone wins

aiShips = placeShips(gameAiMatrix, aiShipMatrix) #place ships onto the gameAI Matrix

#get locations from human player and turn them into a list of pairs

print("second print")
print("ai game matrix:")
print(gameAiMatrix)
print("\n")
print("human game matrix:")
print(gameHumanMatrix)
print("\n")


# FOR TESTING
#get input from user in terminal
humanShips = getHumanInput(gameHumanMatrix, humanShipMatrix)
# TODO - get user input from buttons for user to place ships
   #get locations from user input
   #create ships
   #place ships on board
   # ^^ would normally do this looping to get user input 5 times for 5 ships
   #edge cases:
      #user puts same location that is already taken
      #user puts locations that are not adjacent to each other
    #user puts locations not in a straight line

print("third print")
print("ai game matrix:")
print(gameAiMatrix)
print("\n")
print("human game matrix:")
print(gameHumanMatrix)
print("\n")



#saving variables so they can be used in the next iteration
hit2 = False
ogX, ogY = None, None #keeping track of original targets in case it hits
x2, y2 = None, None 
shipHit = False
directionKnown = False
direction = None
orientationSwitched = False
shipSunk = False

#Human gets to go first

while gameOver == False:
   # Human turn
   # TODO - get human input for target positions
   x1, y1 = humanTurn(aiShipMatrix) #just using this for testing
   #x1, y1 = 1, 1 #SAMPLE FOR NOW

   print("fourth print")
   print("ai game matrix:")
   print(gameAiMatrix)
   print("\n")
   print("human game matrix:")
   print(gameHumanMatrix)
   print("\n")

   
   #updates boards and returns true if hit, false if miss
   hit1 = updateBoards(x1, y1, aiMatrix, gameAiMatrix, aiShipMatrix) 
   if hit1 == True:
      print("HIT!")
      #check if ship has sunk
      ship = aiShipMatrix[x1][y1][0]
      #print(ship)
      if ship.didShipSink() == True:
         print("You have sunk one of my battleships!")
   else:
      print("MISS!")
   printAiBoard(aiShipMatrix)

   
   # TODO - send hit/miss output to human player and let them know if ship has sunk
   # TODO - update LED boards based off of hit/miss

   gameOver = isGameOver(aiShips)
   if gameOver == True: #if human wins game
      print("Congratulations! You won!")
      break

   #TODO - AI Turn
      # get most likely location to hit
      # if there was no hit, find the most likely location again
      # if there was a hit, find most likely orientation
      # if guess all in one direction and still not sunk, change direction


   # AI Turn

   if shipHit == False: #if no ship has been hit, look for regular target
      
      #do it in the if statement because we dont want to target another ship if we are already targeting a ship
      #if a ship is hit in the process of sinking another ship than it is only possible
      #for it to have been hit once unless it is in the same direction in which case
      #it would been sunk
      for humanShip in humanShips:
         if humanShip.hits > 0 and humanShip.sunk == False: #ship was hit and not sunk
            shipHit = True
            hitLocations = []
            for location in humanShip.locations:
               if location[2] == True:
                  hitLocations.append((location[0], location[1]))
                  ogX, ogY = location[0], location[1]
                  x2, y2 = ogX, ogY
            # numHits = len(hitLocations)
            # if numHits > 1: #then shit hit at least twice
            #    x2, y2 = humanShip.locations[numHits-1][0], humanShip.locations[numHits-1][1]

            #    direction = highestProbDirection(ogX, ogY, x2, y2, gameHumanMatrix)
            #    directionKnown = True


               #get direction of the ship
               # if x2 == ogX: #if same row
               #    #we check which direction (east/west) will have the higher probability
               #    direction = highestProbDirection()
                  
               # elif y2 == ogX: #if same column
               #    #we check which direction (north/south) will have the higher probability
               #    direction = highestProbDirection()

               # directionKnown = True

            break; #break once we do this for the first ship we find



      x2, y2 = aiMove(gameHumanMatrix)
      print("this is where we are")
      print(x2, y2)
      ogX, ogY = x2, y2
      hit2 = updateBoards(x2, y2, humanMatrix, gameHumanMatrix, humanShipMatrix)
      shipHit = hit2

   elif shipHit == True:

      if directionKnown == False:
         #xStart, yStart = x2, y2
         x2, y2, direction = getShipDirection(x2, y2)
         print(gameHumanMatrix)
         hit2 = updateBoards(x2, y2, humanMatrix, gameHumanMatrix, humanShipMatrix)
         directionKnown = hit2 #direction only known if there is a hit nearby

         #need to check that we hit the same ship
         #if humanShipMatrix[x][y] == humanShipMatrix[x2][y2]: #then same ship
         #   directionKnown = hit2 #we only know direction if hit same ship

         #else: #hit different ship




      # need to save original hit in case we need to switch direction

      elif directionKnown == True:
         if hit2 == True:
            x2, y2, direction = hitShip(x2, y2, direction, ogX, ogY)
            hit2 = updateBoards(x2, y2, humanMatrix, gameHumanMatrix, humanShipMatrix)


         elif hit2 == False: #if not sunk and miss

            if orientationSwitched == False:
               x2, y2, direction = switchOrientation(ogX, ogY, direction)
               hit2 = updateBoard(x2, y2, humanMatrix, gameHumanMatrix, humanShipMatrix)
               orientationSwitched == True

            else:
               x2, y2, direction = getShipDirection(x2, y2)
               hit2 = updateBoards(x2, y2, humanMatrix, gameHumanMatrix, humanShipMatrix)


            #if switch orientation has been called and still no hit, we need to try another direction


            #humanShipMatrix[x][y]

            #x2, y2, direction = getShipDirection(x2, y2, direction)

   if hit2 == True:
      print("The AI HIT one of your ships!")
   else:
      print("The AI MISSED!")
   printHumanBoard(humanShipMatrix)

   #check if original target ship has sunk
   if humanShipMatrix[ogX][ogY] != 0 and humanShipMatrix[ogX][ogY] != "O":
      ship = humanShipMatrix[ogX][ogY][0]
      shipSunk = ship.didShipSink()
      if shipSunk == True: #reset variables
         print("Sunk ship of size ", ship.length)
         hit2 = False
         ogX, ogY = None, None #keeping track of original targets in case it hits
         x2, y2 = None, None 
         shipHit = False
         directionKnown = False
         direction = None
         orientationSwitched = False
         shipSunk = False
         humanShips.remove(ship)

         #TODO - lights of ship blink 10-15 times to show that is has sunk


   #check all ships to see if any of them have sunk in case it was not OG ship
   #but we only want to see if it was newly sunk so if a ship is sunk we take it out of the list
   # for humanShip in humanShips:
   #    if humanShip.sunk == True:
   #       humanShips.remove(ship)
   #       x2, y2 = ogX, ogY
   #       hit2 = False
         


   
   # just for now until we have this fully functional
   #gameOver = True
   #print("we are here")
   #print(humanShips)
   gameOver = isGameOver(humanShips)
   if gameOver == True: #if AI wins game
      print("Congratulations! You won!")

   #print(gameOver)

   # TODO - when game is over, have all lights on the board blinking
   # When game is over, make lights blink in cool shape (start going in and out? bordere going in and out?)

   # TODO - send hit/miss output to human player
   # TODO - update LED boards based off of hit/miss






gamesPlayed = gamesPlayed + 1; #increment number of games played
gamesPlayedFile = open("gamesPlayed.txt", "w")
gamesPlayedFile.write(str(gamesPlayed)) #save to file to be used in next game
gamesPlayedFile.close()

# These files contain the probability matrices at the end of this game that
# should be used at the start of the next game...
# Here we are writing the values to the files

#writing humanMatrix to file
humanMatrixFile = open("humanMatrix.txt", "w")
for row in humanMatrix:
   #print(row)
   for value in row:
      humanMatrixFile.write(str(value) + "\n")
humanMatrixFile.close()

#writing aiMatrix to file
aiMatrixFile = open("aiMatrix.txt", "w")
for row in aiMatrix:
   #print(row)
   for value in row:
      aiMatrixFile.write(str(value) + "\n")
aiMatrixFile.close()






