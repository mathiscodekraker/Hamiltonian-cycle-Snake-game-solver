#library
import OpenWebsiteAndStartGame as OWASG
from OpenWebsiteAndStartGame import GameScreenSize
from PIL import ImageGrab

#screenshot devide image into grid 
#- from PIL import Image https://codingfleet.com/transformation-details/splitting-an-image-into-a-grid-using-python/

def SnakeMoved(img):
    return
    
#function
def MoveSetCompletion(SpacesHaveToMoveAmount, Direction):
    for each in range(SpacesHaveToMoveAmount):
        SnakeNotMoved = True
        while SnakeNotMoved:
            img = ImageGrab.grab(bbox=GameScreenSize)
            SnakeNotMoved = not SnakeMoved(img)
            pass
        pass
    pass
