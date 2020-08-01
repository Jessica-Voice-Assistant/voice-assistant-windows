import pyautogui
pyautogui.FAILSAFE = True
def spotifySkill():
    sp1 = None
    while sp1 is None:
        sp1 = pyautogui.locateOnScreen('sp1.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(sp1)
    pyautogui.click()
    pyautogui.click()