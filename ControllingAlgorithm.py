#Librarys
import Controlls as C
import ImageRecognition as IR
import OpenWebsiteAndStartGame as OWASG
from PIL.ImageCms import Direction

#variables
#Constant Variables
FromStart = ["From Start", "from start", "*From Start*", "*from start*", "FromStart"]

#sub move lists
HorizantalSubList = [[4, 1], [3, 1], [4, 1], [1, 1]]
VerticalSubList = [[1, 1], [4, 19], [1, 1], [2, 19]]

#move set after reaching specific point 0=nothing/stay on course 1 = up, 2 = right, 3 = down, 4 = left
StartMoveSet = []
StartDirection = -1
Position = []

#follow the paths one at a time 2A then 2B
#start in the right in the bottom
#first is direcion second is how many squires it moves
LeftRight = [VerticalSubList*6]
#19keer 4
UpDown = [[1, 2], HorizantalSubList*9, [4, 1]]
FoundationalMoveSet1 = LeftRight + UpDown
FoundationalMoveSet2A = [[3, 1], [4, 1], [3, 1]]
FoundationalMoveSet2B = [[0, 1], [3, 2]]
FoundationalMoveSet3 = [[0, 12], [2, 20]]

#functions
def Move(InputValue):
    if InputValue == 1:
        C.MoveUp()
    elif InputValue == 2:
        C.MoveRight()
    elif InputValue == 3:
        C.MoveDown()
    elif InputValue == 4:
        C.MoveLeft()
    else:
        print("error: wrong input for the move set")
        pass
    pass

def ExecuteMoveSet(Inputs):
    global Position
    if Inputs[0] != 0:
        Move(Inputs[0])
    else:
        Inputs[0]  = StartDirection
        pass
    Position = IR.MoveSetCompletion(Inputs[1], Inputs[0], Position)
    pass

def ExecuteEachMove(InputsList):
    global StartDirection
    for index, each in enumerate(InputsList):
        ExecuteMoveSet(each)
        pass
    pass

#Execution
def ChooseWhatVersionToExecute():
    global StartMoveSet, StartDirection, StartPosition
    ChooseInput = input("what version do you execute: ")
    if ChooseInput in FromStart:
        StartMoveSet = [[0, 11], [2, 10]]
        StartDirection = 3
        StartPosition = [11, 4]

        print("1. slug")
        print("2. worm")
        print("3. python")
        VersionOfTheGame = input("which of the games do you want the program to play enter the number: ")
        OWASG.StartGame(int(VersionOfTheGame))
        pass
    pass

while True:
    #here could be a function that opens the game
    ChooseWhatVersionToExecute()
    Position = StartPosition
    ExecuteEachMove(StartMoveSet)
    MoveSet1 = True
    while True:
        ExecuteEachMove(FoundationalMoveSet1)
        if MoveSet1:
            ExecuteEachMove(FoundationalMoveSet2A)
            MoveSet1 = False
        else:
            ExecuteEachMove(FoundationalMoveSet2B)
            MoveSet1 = True
            pass
        ExecuteEachMove(FoundationalMoveSet3)
        pass
    pass
