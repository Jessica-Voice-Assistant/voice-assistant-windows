import pyautogui
import time
import keyboard
import random
import win32api, win32con
pyautogui.FAILSAFE = True
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def playpianotiles():
    while keyboard.is_pressed('q') == False:
        if pyautogui.pixelMatchesColor(525, 520, ( 59,  56,  63))==True:
            click(525, 520)
        if pyautogui.pixelMatchesColor(626, 520, ( 59,  56,  63))==True:
            click(626, 520)
        if pyautogui.pixelMatchesColor(739, 520, ( 59,  56,  63))==True:
            click(739, 520)
        if pyautogui.pixelMatchesColor(843, 520, ( 59,  56,  63))==True:
            click(843, 520)