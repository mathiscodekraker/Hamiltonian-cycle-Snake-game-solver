#Librarys
import Controlls as C
import ImageRecognition as IR
import OpenWebsiteAndStartGame as OWASG

#variables
#Constant Variables
FromStart = ["From Start", "from start", "*From Start*", "*from start*", "FromStart"]
#move set after reaching specific point 1 = up, 2 = right, 3 = down, 4 = left
FoundationalMoveSet = []

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
