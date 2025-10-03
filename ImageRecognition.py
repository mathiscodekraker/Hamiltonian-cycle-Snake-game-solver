#library
import OpenWebsiteAndStartGame as OWASG
from OpenWebsiteAndStartGame import GameScreenSize
from OpenWebsiteAndStartGame import BlockSize
from PIL import ImageGrab
import cv2
import numpy as np

#variables
#Constant Variables
XAndYBlocks = [21, 15]
BlockPNG = cv2.imread("snake block.png", cv2.IMREAD_COLOR)

#function
def DevideImageInTiles(img):
    TileDic = {}
    ImageCV = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    for y in range(0, (XAndYBlocks[1]*BlockSize[1]), BlockSize[1]):
        for x in range(0, (XAndYBlocks[0]*BlockSize[0]), BlockSize[0]):
            tile = ImageCV[y:y + BlockSize[1], x:x + BlockSize[0]]
            TileDic[(x/BlockSize[0], y/BlockSize[1])] = tile
    return TileDic

def ReturnExpectedLocation(Direction, Location):
    if Direction == 1:
        XY = [1, 0]
    elif Direction == 3:
        XY = [-1, 0]
    elif Direction == 2:
        XY = [0, 1]
    elif Direction == 4:
        XY = [0, -1]
        pass
    print(Direction)
    ExpectedLocation = [(Location[0] + XY[0]), (Location[1] + XY[1])]
    return ExpectedLocation

def SnakeMoved(TilesList, Direction, Location):
    ExpectedLocation = ReturnExpectedLocation(Direction, Location)

    Tile = TilesList[(ExpectedLocation[0], ExpectedLocation[1])]
    Result = cv2.matchTemplate(Tile, BlockPNG, cv2.TM_CCOEFF_NORMED)
    _, MaxVal, _, _ = cv2.minMaxLoc(Result)
    return (MaxVal >= 0.8)

def MoveSetCompletion(SpacesHaveToMoveAmount, Direction, Location):
    for each in range(SpacesHaveToMoveAmount):
        SnakeNotMoved = True
        print("HEHO")
        while SnakeNotMoved:
            img = ImageGrab.grab(bbox=GameScreenSize)
            TilesList = DevideImageInTiles(img)
            SnakeNotMoved = not SnakeMoved(TilesList, Direction, Location)
            print("WHAT: ", SnakeNotMoved)
            pass
        Location = ReturnExpectedLocation(Direction, Location)
        pass
    return Location
