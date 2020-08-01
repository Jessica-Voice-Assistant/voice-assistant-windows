import pyautogui
pyautogui.FAILSAFE = True
def securitySkill():
    df1 = None
    df2 = None
    while df1 is None:
        df1 = pyautogui.locateOnScreen('df1.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(df1)
    pyautogui.click()
    while df2 is None:
        df2 = pyautogui.locateOnScreen('df2.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(df2)
    pyautogui.click()