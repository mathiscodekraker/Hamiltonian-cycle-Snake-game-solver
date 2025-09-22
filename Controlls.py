#librarys 
import keyboard as key

#Constant variables
#make controll functions (wasd or up down left right arrows two options)
Up = "w"
Down = "s"
Left = "a"
Right = "d"

#functions
#move functions
def Move(WantedInputKey):
    key.send(WantedInputKey)
    pass

def MoveUp():
    Move(Up)
    pass

def MoveDown():
    Move(Down)
    pass

def MoveLeft():
    Move(Left)
    pass

def MoveRight():
    Move(Right)
    pass


