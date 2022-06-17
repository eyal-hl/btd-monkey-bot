import pyautogui, ctypes
from monkeTower import MonkeyTower
import time
from config import offset

VILLAGE_POS = (850, 332)
SUPER_MONKEY_POS = (770, 413)
NINJA_POS = (864, 431)
ALCHAM_POS = (682, 207)

#(31, 37, 47) ???
ALCHEMY_BUTTON = 'f'
NINJA_BUTTON = 'd'
VILLAGE_BUTTON = 'k'
SUPER_MONKE_BUTTON = 's'

PLAY_BUTTON_POS = (1815, 1017)
PLAY_BUTTON_PLAYING_COLOR = (255, 255, 255)
PLAY_BUTTON_WON_COLOR = (65, 65, 65)
PLAY_BUTTON_LVLUP_COLOR = (105, 105, 105) # press 2 times

NEXT_BUTTON_POS = (967, 908)
FREEPLAY_BUTTON_POS = (1128, 849)
RESTART_BUTTON_POS = (1071, 849)
CONFIRM_RESTART_BUTTON_POS = (1137, 722)

village = MonkeyTower(VILLAGE_BUTTON, VILLAGE_POS, (2,0,2))
super_monke = MonkeyTower(SUPER_MONKE_BUTTON, SUPER_MONKEY_POS, (2,0,3))
ninja = MonkeyTower(NINJA_BUTTON, NINJA_POS, (3,0,1))
alcham = MonkeyTower(ALCHEMY_BUTTON, ALCHAM_POS, (3,0,0))

def place_monkes():
    village.placeAndUpgrade()
    super_monke.placeAndUpgrade()
    ninja.placeAndUpgrade()
    alcham.placeAndUpgrade()


def restart_after_finish():
    ctypes.windll.user32.SetCursorPos(NEXT_BUTTON_POS[0] + offset, NEXT_BUTTON_POS[1])
    pyautogui.click()
    time.sleep(0.6)
    ctypes.windll.user32.SetCursorPos(FREEPLAY_BUTTON_POS[0] + offset,FREEPLAY_BUTTON_POS[1])
    pyautogui.click()
    time.sleep(0.6)
    pyautogui.press('enter')
    time.sleep(0.6)
    pyautogui.press('escape')
    time.sleep(0.6)

    ctypes.windll.user32.SetCursorPos(RESTART_BUTTON_POS[0] + offset, RESTART_BUTTON_POS[1])
    pyautogui.click()
    time.sleep(0.6)
    ctypes.windll.user32.SetCursorPos(CONFIRM_RESTART_BUTTON_POS[0] + offset,CONFIRM_RESTART_BUTTON_POS[1])
    pyautogui.click()
    time.sleep(0.6)


def play():
    for i in range(2): pyautogui.typewrite(' ')

    while True:
        time.sleep(10)
        state_color = pyautogui.pixel(PLAY_BUTTON_POS[0] + offset, PLAY_BUTTON_POS[1])
        if state_color == PLAY_BUTTON_PLAYING_COLOR:
            continue
        elif state_color == PLAY_BUTTON_WON_COLOR:
            break
        elif state_color == PLAY_BUTTON_LVLUP_COLOR:
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.click()
            pyautogui.typewrite(' ')
            print('lvled up!')
        elif state_color == (31, 37, 47):
            continue
        else:
            print(state_color)
            quit(0)



# print(pyautogui.position())
time.sleep(1)
for i in range(130):
    starting_time = time.time()
    print('starting the',i+1,'round')
    place_monkes()
    play()
    restart_after_finish()