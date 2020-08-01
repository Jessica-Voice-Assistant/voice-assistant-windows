import pyautogui
pyautogui.FAILSAFE = True
def updateSkill():
    u1 = None
    u2 = None
    while u1 is None:
        u1 = pyautogui.locateOnScreen('u1.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(u1)
    pyautogui.click()
    while u2 is None:
        u2 = pyautogui.locateOnScreen('u2.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(u2)
    pyautogui.click()