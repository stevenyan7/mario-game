#Assignment 4 - My_Mario_Version_1.py
#
#This Mario game can let user input a location of a maze, such as "4 7"
#And "Mario" can go to the location where user input
#There are also rewards and exploding obstacles in the maze!
#
#Chu Yan
#Yaben Yang
#March 20, 2016



#function of users' input
def askInput(maze, upperBound, lowerBound):
    userInput = input("""Enter Mario's location by entering a row integer number (1 <= row <= 12)
and a column integer number (1 <= colum <= 15):""")
    if userInput == "":#check if it is empty str
        print("You have not entered a thing!")
    elif userInput.isalpha():#check if it is a word
        print("You have entered %s. Please, try again."%userInput)
    
    else:
        userInput = userInput.split()
        if len(userInput)== 1:#check if it contains just 1 number
            print("You have entered only 1 number, i.e., %s. Please, try again."%userInput)
        elif len(userInput)> 2:#check if it contains more than 2 number
            print("You have entered more than 2 numbers, i.e., [%s]. Please, try again."%userInput)
        elif not(userInput[0].isdigit()) or not(userInput[1].isdigit()):#check if it is floating number
            print("You have entered floating point number(s), i.e., [%s]. Please, try again."%userInput)
        elif int(userInput[0])>12 or int(userInput[1])>15 or int(userInput[0])<1 or int(userInput[1])<1:#check if it is out of range
            print("Row and/or column number ( %s  ) are out of range"%userInput)
        
        else:
            inputRow = int(userInput[0])-1
            inputColumn = int(userInput[1])-1
            if maze[inputRow][inputColumn] =="R" or maze[inputRow][inputColumn] =="E" :#check if it is occupied
                
                print("This cell is occupied. Please, try again.")
            else:
                maze[inputRow][inputColumn] = "M"#change . to M
                if inputRow<=6:
                    if inputColumn<7:#area A
            
                        lowerBound = "   -------------------------- = ----------------"
                    else:#area B
                        lowerBound = "   --------------- = ---------------------------"
                else:
                    if inputColumn<7:#area c
                        upperBound = "   -------------------------- = ----------------"
                    else:#area D
                        upperBound = "   --------------- = ---------------------------"
                printMaze(maze, upperBound, lowerBound)
                print("-------")

#create a function of creating a maze                   
def createMaze(mazeHeight, mazeWidth):
    maze = list()
    for i in range(mazeHeight):
        mazeRow = list()
        for i in range(mazeWidth):
            mazeRow.append(".")
        maze.append(mazeRow)
    return maze

#create a function of printing maze
def printMaze(maze, upperBound, lowerBound):
    print ("    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 ")
    print (upperBound)
    index = 1
    for i in maze:
        if index<10:
            mazeRow = str(index)+" |"
        else:
            mazeRow = str(index)+"|"            
        index += 1
        for x in i:
            mazeRow = mazeRow + " " + x + " "
        print(mazeRow+"|")
    print(lowerBound)
    print("\n")
    return maze

import random #import random functions

#add rewards and exploding obstacles into the maze
def add(item, maze, times):
    height = len(maze)-1
    width = len(maze[0])-1
    for i in range(times):
        row = random.randint(0, height)
        column = random.randint(0, width)
        while maze[row][column] != ".":
            row = random.randint(0, height)
            column = random.randint(0, width)
        maze[row][column] = item
    return maze



        
#main
mazeHeight = 12
mazeWidth = 15
aNumOfExplodingObstacles = 20
aNumOfRewardingObstacles = 20
maze = createMaze(mazeHeight, mazeWidth)
upperBound = "   ---------------------------------------------"
lowerBound = "   ---------------------------------------------"

add("R", maze, 20)
add("E", maze, 20)
printMaze(maze, upperBound, lowerBound)
askInput(maze, upperBound, lowerBound)




