#Assignment 5 - My_Mario_Version_2.py
#
##The goal of our Assignment 5 is to allow the player (user) to play our game by moving Mario
##around the maze.

#There are also rewards and exploding obstacles in the maze!
#
#Chu Yan
#Yaben Yang
#April 8, 2016

import random

def playGame(score,MPosition, rewardingObstaclesList, explodingObstaclesList, maze,emptyMazCell):

    MPositionList = MPosition
    
    while score>0 :
        #promot user input + validation
        userChoose = userInput(mazeHeight, mazeWidth, MPosition)
        if userChoose == "x":
            print("\n")
            print("------")
        #if exit
        elif  userChoose == "exit":
            print("\n")
            print("Mario has reached the exit gate with a score of %i! You win!" %score)
        else:
                if userChoose == "u":
                    MPositionList[0]-=1
                elif userChoose == "d":
                    MPositionList[0]+=1
                elif userChoose == "l":
                    MPositionList[1]-=1
                elif userChoose == "r":
                    MPositionList[1]+=1
            
                testList=str(MPosition[0])+' '+str(MPosition[1])
        
                
                if testList in rewardingObstaclesList:
  
                    score += 1
                elif testList in explodingObstaclesList:

                    score -= 1
                turnMapCellToNormal(maze,MPositionList, emptyMazCell)
                
                maze = createMaze(mazeHeight, mazeWidth, emptyMazCell)
                


                addItem(symbolOfExplodingObstacles, maze, aNumOfRewardingObstacles, rewardingObstaclesList)
                addItem(symbolOfRewardingObstacles, maze, aNumOfExplodingObstacles,explodingObstaclesList)

                Mario(maze,symbolOfMario,symbolOfGate, topBoundary, botBoundary, topBotBorder, MPosition, score)
                
                playGame(score,MPosition, rewardingObstaclesList, explodingObstaclesList, maze,emptyMazCell)
        return


        

        

#create a function of creating maze
def createMaze(mazeHeight, mazeWidth, emptyMazCell):
    maze = list()
    for i in range(mazeHeight):
        row = list()
        for i in range(mazeWidth):
            row.append(emptyMazCell)
        maze.append(row)
    
    return maze

#draw frame of maze
def mazeFrame(maze, rowNum, columnNum, topBoundary, botBoundary, leftRightBorder):
    
    print("\n")
    topNum = list()
    for topNum in range(1, columnNum + 1):
        columnNum = list()
        if topNum == 1:
            columnNum = "    " + str(topNum) + " "
        elif topNum < 10:
            columnNum = str(topNum) + " "
        else:
            columnNum = str(topNum) + ""
        print (columnNum, end=" ")
    #print top boundary
    print(topBoundary)
    sideNum = 1
    for i in maze:
        if sideNum < 10:
            rowNum = str(sideNum)+" "+leftRightBorder
        else:
            rowNum = str(sideNum)+leftRightBorder           
        sideNum += 1
        for c in i:
            rowNum += " " + c + " "
        print (rowNum + leftRightBorder)
    #print bottom boundary
    print(botBoundary)
    return maze



#draw random obstacles
def addItem(name, maze, amount, objectList):

    for i in range(amount):
 
        r = int(objectList[i].split()[0])
        c = int(objectList[i].split()[1])
        
        maze[r][c] = name
    return maze

#initial mario's location from user
def Mario(maze, mario, gate, topBoundary, botBoundary, topBotBorder, MPosition, score):
 
    theParts = MPosition  
           
    userR = int(theParts[0])
    userC = int(theParts[1])
    maze[userR][userC] = mario
    if userC < int(mazeWidth/2):
        if userC < int(mazeWidth/2):
            num = random.randint(0,1)
            if num == 1:
                botBoundary = "   " + (topBotBorder * mazeWidth)[:-1]+gate
                topBoundary = "\n   " + topBotBorder * mazeWidth
            else:
                topBoundary = "\n   " + (topBotBorder * mazeWidth)[:-1]+gate
                botBoundary = "   " + topBotBorder * mazeWidth
        else:
            num = random.randint(0,1)
            if num == 1:
                botBoundary = "   " + gate + (topBotBorder * mazeWidth)[:-1]
                topBoundary = "\n   " + topBotBorder * mazeWidth
            else:
                topBoundary = "\n   " + gate + (topBotBorder * mazeWidth)[:-1]
                botBoundary = "   " + topBotBorder * mazeWidth

                    
            botBoundary = "   " + topBotBorder * mazeWidth + "\n\n-------"
    mazeFrame(maze, mazeHeight, mazeWidth, topBoundary, botBoundary, leftRightBorder)
        
                    
    print("Mario's score -> ",score)
    print("\n")

def userInput(mazeHeight, mazeWidth, MPosition):
    MPositionList = MPosition
    userChoose = input("Move Mario by entering the letter 'r' for right, 'l' for left, 'u' for up and 'd' for down, 'x' to exit the game: ")
    userChoose = userChoose.lower()
    #validation
    allowList = ['u', 'd', 'l', 'r','x']
    
    while (userChoose.lower() not in allowList) :
        userChoose = input("Invalid input or cannot move, please Enter a direction: ")
    
    return userChoose
def turnMapCellToNormal(maze,MPositionList, emptyMazCell):
    maze[MPosition[0]][MPosition[1]] = emptyMazCell
    

 

        

        
#Main
print("Welcome to my Mario game.") 


#read file
##inputFile = 'InputData_Assn_5_1.txt'
inputFile = input("Please, enter a filename: ")

# Opening a file for reading
fileR = open(inputFile, 'r')

myDataList = list(fileR)

#remove \n for each data file line
for i in range(len(myDataList)):
    myDataList[i] =    myDataList[i].strip()

mazeHeight = int(myDataList[1])
mazeWidth = int(myDataList[0])
aNumOfExplodingObstacles = int(myDataList[3])
aNumOfRewardingObstacles = int(myDataList[2])
emptyMazCell = myDataList[4]

symbolOfExplodingObstacles = myDataList[5]
symbolOfRewardingObstacles = myDataList[6]

symbolOfMario = myDataList[7]
symbolOfGate = myDataList[8]

topBotBorder = myDataList[9]
leftRightBorder = myDataList[10]
topBoundary = "\n   " + topBotBorder * mazeWidth
botBoundary = "   " + topBotBorder * mazeWidth + "\n"

MPosition = myDataList[11]
MPosition = (MPosition.split())

#re-structure MPosition to [int, int]
MPosition[0] = int(MPosition[0])
MPosition[1] = int(MPosition[1])
rewardingObstaclesList = myDataList[12:12+aNumOfRewardingObstacles]
explodingObstaclesList = myDataList[12+aNumOfRewardingObstacles:]

score = aNumOfExplodingObstacles//3

maze = createMaze(mazeHeight, mazeWidth, emptyMazCell)

addItem(symbolOfExplodingObstacles, maze, aNumOfRewardingObstacles, rewardingObstaclesList)
addItem(symbolOfRewardingObstacles, maze, aNumOfExplodingObstacles,explodingObstaclesList)

Mario(maze,symbolOfMario,symbolOfGate, topBoundary, botBoundary, topBotBorder, MPosition, score)

playGame(score,MPosition, rewardingObstaclesList, explodingObstaclesList, maze,emptyMazCell)


