#Librarys
import Controlls as C
import ImageRecognition as IR
import OpenWebsiteAndStartGame as OWASG

#variables
#Constant Variables
FromStart = ["From Start", "from start", "*From Start*", "*from start*", "FromStart"]
#move set after reaching specific point 1 = up, 2 = right, 3 = down, 4 = left
#follow the paths one at a time 2A then 2B
#start in the right in the bottom
LeftRight = [1, 4, 1, 2, 1, 4, 1, 2, 1, 4, 1, 2, 1, 4, 1, 2, 1 4, 1, 2, 1, 4, 1, 2]
#19keer 4
UpDown = [1, 4, 3, 4, 1, 4, 3, 4, 1, 4, 3, 4, 1, 4, 3, 4, 1, 4, 3, 4, 1, 4, 3, 4, 1, 4, 3, 4, 1, 4, 3, 4, 1, 4, 3, 4, 1, 4]
FoundationalMoveSet1 = LeftRight + UpDown
FoundationalMoveSet2A = [3, 4]
FoundationalMoveSet2B = [3]
FoundationalMoveSet3 = [2]

#functions
def Move(InputValue):
    if InputValue == 1:
        C.MoveUp()
    elif InputValue == 2:
        MoveRight()
    elif InputValue == 3:
        MoveDown()
    elif InputValue == 4:
        MoveLeft()
    else:
        print("error: wrong input for the move set")
        pass
    pass

#Execution
def ChooseWhatVersionToExecute():
    ChooseInput = input("what version do you execute: ")
    if ChooseInput in FromStart:
        pass
    pass

while True:
    ChooseWhatVersionToExecute()
    pass
