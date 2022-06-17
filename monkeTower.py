import pyautogui, ctypes
import time
from config import offset


LVL_TOP = ','
LVL_MID = '.'
LVL_BOT = '/'

class MonkeyTower():

    def __init__(self, monke_button, monke_pos, monke_lvls):
        self.button = monke_button
        self.pos = monke_pos
        self.lvls = monke_lvls

    def placeAndUpgrade(self):
        self.place()
        time.sleep(0.2)
        self.upgrade()


    def place(self):
        ctypes.windll.user32.SetCursorPos(self.pos[0] + offset, self.pos[1])
        pyautogui.press(self.button)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.click()

    def upgrade(self):
        for i in range(self.lvls[0]): pyautogui.press(LVL_TOP)
        for i in range(self.lvls[1]): pyautogui.press(LVL_MID)
        for i in range(self.lvls[2]): pyautogui.press(LVL_BOT)
        time.sleep(0.7)