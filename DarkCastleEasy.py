import pyautogui, time
from monkeTower import MonkeyTower
from globalFunctions import restart_after_finish
SUB_POS = (1097, 421)
SUB_BUTTON = "x"

BEN_POS = (964, 63)
BEN_BUTTON = "u"

DART_POS = (569, 478)
DART_BUTTON = "q"

WIZARD_POS = (969, 394)
WIZARD_BUTTON = "a"

NINJA_POS = (855, 433)
NINJA_BUTTON = "d"

sub = MonkeyTower(SUB_BUTTON,SUB_POS,(0,0,0))
ben = MonkeyTower(BEN_BUTTON, BEN_POS, (0,0,0))
dart = MonkeyTower(DART_BUTTON, DART_POS, (0,2,3))
wizard = MonkeyTower(WIZARD_BUTTON, WIZARD_POS, (0,2,0))
ninja = MonkeyTower(NINJA_BUTTON, NINJA_POS, (4,0,2))
if __name__ == '__main__':
    time.sleep(1)

    for i in range(40):
        print(i)
        sub.placeAndUpgrade()
        for i in range(2): pyautogui.typewrite(' ')
        time.sleep(34) # enough time to have money for BEN

        ben.place()
        dart.place()
        time.sleep(40) # enough time to have money for dart upgrades
        dart.upgrade()
        time.sleep(40) # enougth time to have money for wall of fire
        wizard.placeAndUpgrade()
        time.sleep(100) # get money for the ninja
        ninja.placeAndUpgrade()
        time.sleep(120) # the game should be over
        restart_after_finish()
