import sys
import time
import eel
import skills_engine
import winsound
import pygetwindow as pw
eel.init("frontend_engine")      
@eel.expose
def activatedstatus():
    skills_engine.activatedstatus()
@eel.expose
def recognitiontask(userSaid ,num):
    skills_engine.recognitiontask(userSaid ,num)
@eel.expose
def speakforgui():
    winsound.PlaySound('ready.wav', winsound.SND_FILENAME)
@eel.expose
def invokedstatus():
    winsound.PlaySound('ready.wav', winsound.SND_FILENAME)
    frontend_engine = pw.getWindowsWithTitle('Jessica')[0]
    frontend_engine.restore()
try:
    eel.start('index.html', port=2020, size=(445, 641))
except Exception:
    sys.exit()