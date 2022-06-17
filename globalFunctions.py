import ctypes, pyautogui, time
from config import offset
NEXT_BUTTON_POS = (967, 908)
FREEPLAY_BUTTON_POS = (1128, 849)
RESTART_BUTTON_POS = (1071, 849)
CONFIRM_RESTART_BUTTON_POS = (1137, 722)

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