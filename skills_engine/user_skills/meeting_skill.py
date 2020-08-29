import pyautogui
import subprocess
pyautogui.FAILSAFE = True
id= None
passKey= None
def meetingInit(choice):
    English = 'your  meeting id'
    ComputerS = ''
    Physics = ''
    Chem = ''
    Maths = ''
    PhysicsT = ''
    ChemT = ''
    MathsT = ''
    if choice == 11:
        id= ChemT
        pyautogui.hotkey('win', 'd')
        passKey= pyautogui.prompt(text='Enter password', title='Meeting organiser')
        zoommeetingStart(id, passKey)
    if choice == 21:
        id= PhysicsT
        pyautogui.hotkey('win', 'd')
        passKey= pyautogui.prompt(text='Enter password', title='Meeting organiser')
        zoommeetingStart(id, passKey)
    if choice == 31:
        id= MathsT
        pyautogui.hotkey('win', 'd')
        passKey= pyautogui.prompt(text='Enter password', title='Meeting organiser')
        zoommeetingStart(id, passKey)
    if choice == 1:
        id= English
        ciscomeetingStart(id)
    if choice == 2:
        id= ComputerS
        ciscomeetingStart(id)
    if choice == 3:
        id= Physics
        ciscomeetingStart(id)
    if choice == 4:
        id= Chem
        ciscomeetingStart(id)
    if choice == 5:
        id= Maths
        ciscomeetingStart(id)
    if choice == 6:
        meetingChoose()
def ciscomeetingStart(id):
    pyautogui.hotkey('win', 'd')
    subprocess.Popen('C:\\Program Files (x86)\\Webex\\Webex\\Applications\\ptoneclk.exe')
    b1= None
    c1= None
    d1= None
    while b1 is None:
        b1=pyautogui.locateOnScreen('2.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(b1)
    pyautogui.click(clicks=2)
    pyautogui.write(id)   
    while c1 is None:
        c1=pyautogui.locateOnScreen('3.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(c1)
    pyautogui.click()
    pyautogui.moveTo(b1)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    while d1 is None:
        d1=pyautogui.locateOnScreen('4.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(d1)
    pyautogui.click()
def zoommeetingStart(id, passKey):
    pyautogui.hotkey('win', 'd')
    subprocess.Popen('C:\\Users\\abhid\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
    b= None
    c= None
    d= None
    e= None
    f= None
    while b is None:
        b=pyautogui.locateOnScreen('a.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(b)
    pyautogui.click()
    while c is None:
        c=pyautogui.locateOnScreen('b.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(c)
    pyautogui.click()
    pyautogui.write(id)   
    while d is None:
        d=pyautogui.locateOnScreen('c.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(d)
    pyautogui.click()
    while e is None:
        e=pyautogui.locateOnScreen('d.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(e)
    pyautogui.click()
    pyautogui.write(passKey)
    while f is None:
        f=pyautogui.locateOnScreen('e.png', grayscale = True, confidence=.9)
        pyautogui.moveTo(f)
    pyautogui.PAUSE = 1.0
    pyautogui.click()
def meetingChoose():
    pyautogui.hotkey('win', 'd')
    meetingWhat= int(pyautogui.prompt(text='Choose 1. Cisco Webex 2. Zoom', title='Meeting organiser' , default=''))
    if meetingWhat == 1:
        id= pyautogui.prompt(text='Webex:  Enter meeting id/url', title='Meeting organiser' , default='')
        ciscomeetingStart(id)
    if meetingWhat == 2:
        id= pyautogui.prompt(text='Zoom:  Enter meeting id/url', title='Meeting organiser' , default='')
        passKey= pyautogui.prompt(text='Enter password', title='Meeting organiser')
        zoommeetingStart(id, passKey)
