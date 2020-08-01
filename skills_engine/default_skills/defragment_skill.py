import pyautogui
import subprocess
import time
pyautogui.FAILSAFE = True
def defragmentSkill():
    defragui = None
    optimizebutton = None
    mainicon = None
    searchicon = None
    time.sleep(1.5)
    pyautogui.hotkey('win', 's')
    while searchicon is None:
        searchicon = pyautogui.locateOnScreen('d00.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(searchicon)
    pyautogui.click()
    pyautogui.write('defrag')  
    while defragui is None:
        defragui = pyautogui.locateOnScreen('d0.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(defragui)
    pyautogui.click()
    while mainicon is None:
        mainicon = pyautogui.locateOnScreen('d2.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(mainicon)
    pyautogui.click()
    while optimizebutton is None:
        optimizebutton = pyautogui.locateOnScreen('d1.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(optimizebutton)
    pyautogui.click()