#library
import time
import pyautogui

#variables
#constant variables
#590-1330, 289-819 (x=1919, y=1079)
#590-(1919-1330), 289-(1079-819)
#590-589, 289-260
#left top right bottom
GameScreenSize = [590, 290, 1327, 818] #[590, 289, 589, 260]
#snake block size
BlockSize = [32, 32] #[31, 33]
#choose Game Buttons Positions
ChooseGameButtonsPositions = [[733, 695], [927, 695], [1147, 695]]

#functions
def StartGame(VersionOfTheGame):
    #choose game
    WhereToClick = ChooseGameButtonsPositions[(VersionOfTheGame - 1)]
    pyautogui.moveTo(WhereToClick[0], WhereToClick[1])
    pyautogui.click()
    pyautogui.moveTo(0, WhereToClick[1])

    time.sleep(2)
    pass