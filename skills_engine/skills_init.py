# Script containing all instructions to skills
import sys
import eel
import time
import winsound
import pyttsx3 
import pygetwindow as pw
from .user_skills import *
from .default_skills import *
import keyboard
import os
import ctypes
import webbrowser
import pyautogui
speakengine = pyttsx3.init()
voices = speakengine.getProperty('voices') 
speakengine.setProperty('voice', voices[1].id)
speakengine.setProperty('rate', 140)
def rsuccess1():
    winsound.PlaySound('recognized.wav', winsound.SND_FILENAME)
def rsuccess2():
    frontend_engine = pw.getWindowsWithTitle('Jessica')[0]
    frontend_engine.minimize()
    eel.readyState()
def rsuccess3():
    speakengine.runAndWait()
    eel.readyState()
def rsuccess4():
    winsound.PlaySound('recognized.wav', winsound.SND_FILENAME)
    frontend_engine = pw.getWindowsWithTitle('Jessica')[0]
    frontend_engine.minimize()
    eel.readyState()
    pyautogui.hotkey('win', 'd')
def activatedstatus():
    eel.setguimsg('Application is activated!')
    winsound.PlaySound('recognized.wav', winsound.SND_ASYNC)
    speakengine.say('Voice recognition is now activated')
    speakengine.runAndWait()
    frontend_engine = pw.getWindowsWithTitle('Jessica')[0]
    frontend_engine.minimize()
    frontend_engine = pw.getWindowsWithTitle('voiceassistant')[0]
    frontend_engine.minimize()
    eel.set_appstatus(1)
try:
    def recognitiontask(userSaid ,num):
        given_text = userSaid
        text2_clean = '[]"'
        for character in text2_clean:
            given_text = given_text.replace(character, "")
            given_text = given_text.lower()
        #new_text = given_text.split(", ")# same here :)
        #new_text = new_text[0]
        # Add all default and user skills and don't worry much about speed :)
        if 'quit' in given_text:
            rsuccess1()
            frontend_engine = pw.getWindowsWithTitle('Jessica')[0]
            frontend_engine.close()
            sys.exit()
        elif 'hi jessica' in given_text:
            rsuccess1()
            speakengine.say('Hi there ! great to see you !')
            rsuccess3()
        elif 'nevermind' in given_text:
            rsuccess1()
            speakengine.say('Oh, Okay !') 
            rsuccess3()
        elif 'how are you' in given_text:
            rsuccess1()
            speakengine.say('I am doing great till now.. How about you ?')
            speakengine.runAndWait()
            eel.startListening2()
        elif 'i am doing great' in given_text:
            rsuccess1()
            speakengine.say("That's realy good... I hope your day goes well.")
            rsuccess3()
        elif 'not so good' in given_text:
            rsuccess1()
            speakengine.say("Don't worry much,.. I hope your day goes well..")
            rsuccess3()
        # You can change it if you want :)
        elif 'who made you' in given_text:
            rsuccess1()
            speakengine.say("I was made by a very kind developer named, Abhishek Das.. Let me take you to his github page")
            rsuccess3()
            webbrowser.open_new('https://github.com/Abhid14')
        elif 'lock pc' in given_text:
            rsuccess1()
            speakengine.say("Locking PC")
            rsuccess3()
            ctypes.windll.user32.LockWorkStation()
        # work to be done below this one     
        elif 'turn off system' in given_text:
            rsuccess1()
            speakengine.say('turning off the system')
            rsuccess3()
        elif 'settings' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\settings')
        elif 'browser' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\edge')
        elif 'google classroom' in given_text:
            rsuccess4()
            webbrowser.open_new('https://classroom.google.com/h')
        elif 'pending assignments' in given_text:
            rsuccess1()
            speakengine.say('checking for pending assisngments')
            rsuccess3()
            webbrowser.open_new_tab('https://classroom.google.com/a/not-turned-in/NzEwMDM1MzUyMjZa')
        elif 'my location' in given_text:
            rsuccess1()
            speakengine.say('showing your location on google maps')
            rsuccess3()
            webbrowser.open_new_tab('https://www.google.com/maps/place/Bengaluru,+Karnataka/&amp')
        elif 'weather' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\weather')
        elif 'pedia' in given_text:
            rsuccess1()
            speakengine.say('Opening wikipedia!')
            rsuccess3()
            webbrowser.open_new('https://wikipedia.com')
        elif 'your favourite song' in given_text:
            rsuccess1()
            speakengine.say("Really ?? you want to hear it ? ..if so okay then .. hope you may like it too and dance like me !!")
            rsuccess3()
            webbrowser.open_new("https://www.youtube.com/watch?v=jl9xKw_xEas")
        elif 'computer'in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\computer')
        elif 'control panel' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\controlpanel')
        elif 'open antivirus' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\security')
        elif 'clock' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\clock')
        elif 'gmail' in given_text:
            rsuccess4()
            webbrowser.open('https://gmail.com')
        elif 'outlook' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\mail')
        elif 'chrome' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\chrome')
        elif 'spotify' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\spotify')
        elif 'open code' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\vscode')
        elif 'amazon prime' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\primevideo')
        elif 'asphalt' in given_text:
            rsuccess4()    
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\asphalt')
        elif 'open calculator' in given_text:
            rsuccess4()  
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\calculator')
        elif 'open calendar' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\calendar')
        elif 'open camera' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\camera')
        elif 'open webex' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\webex')
        elif 'open command' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\cmd')
        elif 'open dropbox' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\dropbox')
        elif 'open download' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\download')
        elif 'open python' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\python')
        elif 'open to do' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\todo')
        elif 'open notepad' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\notepad')
        elif 'open office' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\office')
        elif 'open onedrive' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\onedrive')
        elif 'open photos' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\photos')
        elif 'open paint' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\paint')
        elif 'open zoom' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\zoom')
        elif 'open whatsapp' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\whatsapp')
        elif 'open youtube' in given_text:
            rsuccess4()
            webbrowser.open_new('https://youtube.com')
        elif 'open instagram' in given_text:
            rsuccess4()
            webbrowser.open_new('https://instagram.com')
        elif 'drive fast' in given_text:
            rsuccess4()
            defragmentSkill()
        elif 'system to sleep' in given_text:
            rsuccess4()
            pyautogui.press('sleep')
        elif 'windows updates' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\settings')
            updateSkill()
            speakengine.say("Checking for latest updates from windows..")
            speakengine.runAndWait()
        elif 'quick scan' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\security')
            securitySkill()
            speakengine.say("Scanning for virus and potential threats using windows security.. The task will run in the background..")
            speakengine.runAndWait()
            security_engine = pw.getWindowsWithTitle('Settings')[0]
            security_engine.minimize()
        elif 'take a screenshot' in given_text:
            rsuccess1()
            rsuccess2()
            time.sleep(1)
            pyautogui.press('prntscrn')
            speakengine.say('captured..')
            speakengine.runAndWait()
        elif 'volume' in given_text:
            frontend_engine = pw.getWindowsWithTitle('Jessica')[0]
            frontend_engine.minimize()
            eel.readyState()
            if 'increase' in given_text:
                winsound.PlaySound('recognized.wav', winsound.SND_FILENAME)
                pyautogui.press('volumeup')
            elif 'decrease' in given_text:
                winsound.PlaySound('recognized.wav', winsound.SND_FILENAME)
                pyautogui.press('volumedown')
            elif 'mute' in given_text:
                winsound.PlaySound('recognized.wav', winsound.SND_FILENAME)
                pyautogui.press('volumemute')
            else:
                speakengine.say("Sorry I couldn't Understand that...")
                speakengine.runAndWait()
        elif 'audio' in given_text:
            frontend_engine = pw.getWindowsWithTitle('Jessica')[0]
            frontend_engine.minimize()
            eel.readyState()
            if 'play' in given_text:
                winsound.PlaySound('recognized.wav', winsound.SND_FILENAME)
                pyautogui.press('playpause')
            elif 'pause' in given_text:
                winsound.PlaySound('recognized.wav', winsound.SND_FILENAME)
                pyautogui.press('playpause')
            else:
                speakengine.say("Sorry I couldn't Understand that...")
                speakengine.runAndWait()
        elif 'next track' in given_text:
            winsound.PlaySound('recognized.wav', winsound.SND_FILENAME)
            frontend_engine = pw.getWindowsWithTitle('Jessica')[0]
            frontend_engine.minimize()
            eel.readyState()
            pyautogui.press('nexttrack')
        elif 'previous track' in given_text:
            winsound.PlaySound('recognized.wav', winsound.SND_FILENAME)
            frontend_engine = pw.getWindowsWithTitle('Jessica')[0]
            frontend_engine.minimize()
            eel.readyState()
            pyautogui.press('prevtrack')
            time.sleep(0.5) 
            pyautogui.press('prevtrack') 
        # List of apps ended here :)
        # Add User skills below this comment using elif statements !!
        # And the skills must end with rsuccess(2) or rsuccess(3) else you will have a bad time :)
        elif 'meeting' in given_text:
            try:
                if 'english' in given_text:
                    rsuccess1()
                    meetingInit(1)
                    error_meeting = 0
                elif 'computer meeting' in given_text:
                    rsuccess1()
                    meetingInit(2)
                    error_meeting = 0
                elif 'physics' in given_text:
                    rsuccess1()
                    meetingInit(3)
                    error_meeting = 0
                elif 'chem' in given_text:
                    rsuccess1()
                    meetingInit(4)
                    error_meeting = 0
                elif 'math' in given_text:
                    rsuccess1()
                    meetingInit(5)
                    error_meeting = 0
                    error_meeting = 0
                elif 'manual' in given_text:
                    rsuccess1()
                    meetingInit(6)
                    error_meeting = 0
                else:
                    speakengine.say("Sorry I couldn't find that meeting!")
            except Exception:
                speakengine.say("error occured while execution")
            if error_meeting == 0:
                speakengine.say("execution successfull")
            rsuccess3()
            error_meeting = None
            frontend_engine = pw.getWindowsWithTitle('Jessica')[0]
            frontend_engine.minimize()
        elif 'coaching' in given_text:
            try:
                if 'chem' in given_text:
                    rsuccess1()
                    meetingInit(11)
                    error_meeting = 0
                elif 'phy' in given_text:
                    rsuccess1()
                    meetingInit(21)
                    error_meeting = 0
                elif 'math' in given_text:
                    rsuccess1()
                    meetingInit(31)
                    error_meeting = 0
                else:
                    speakengine.say("Sorry I couldn't find that meeting!")
            except Exception:
                speakengine.say("error occured while execution")
            if error_meeting == 0:
                speakengine.say("execution successfull")
            rsuccess3()
            error_meeting = None
            frontend_engine = pw.getWindowsWithTitle('Jessica')[0]
            frontend_engine.minimize()
        elif 'is anand' in given_text:
            rsuccess1()
            try:
                os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\user_skills\ananda.jpg')
                time.sleep(3)
                speakengine.say('Look at him this is whom you are asking for I guess!!')
            except Exception:
                speakengine.say("I am sorry to say but I don't know that person !")
            rsuccess3()
        elif 'girlfriend' in given_text:
            rsuccess1()
            speakengine.say('i have heard that His girlfriend is Ambika')
            rsuccess3()
        elif 'country' in given_text:
            rsuccess1()
            webbrowser.open_new('https://www.google.com/maps/place/China/&amp')
            time.sleep(5)
            speakengine.say('I am afraid to say but this is where he belongs to .. oh my gosh !!')
            rsuccess3()
        elif 'favourite song' in given_text:
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\spotify')
            spotifySkill()
            speakengine.say('Playing your favourite songs on spotify..')
            speakengine.runAndWait()
        elif 'do you love me' in given_text:
            rsuccess1()
            speakengine.say("You will soon know the answer to this question...")
            rsuccess3()
            webbrowser.open_new('https://www.youtube.com/watch?v=jzD_yyEcp0M&feature=youtu.be&t=9')
        elif 'say hi to carry' in given_text:
            rsuccess1()
            speakengine.say('hii bro !!')
            rsuccess3()
            time.sleep(1.3)
            winsound.PlaySound('recognized.wav', winsound.SND_FILENAME)
        elif 'piano tiles skills' in given_text:
            rsuccess1()
            speakengine.say('I would love to play piano tiles just if I make any error be sure to press q on your keyboard')
            speakengine.runAndWait()
            rsuccess4()
            os.startfile(r'C:\Users\abhid\Desktop\Voice Assistant\skills_engine\default_skills\shortcuts\piano')
            playpianotiles()
            speakengine.say("I hope you liked it !!")
            speakengine.runAndWait()
            piano_window = pw.getWindowsWithTitle('Piano White Master!')[0]
            piano_window.close()
        # Don't touch anything below this warning !!
        else:
            if num ==1:
                eel.set_appstatus(3)
                speakengine.say("Sorry I didn't understand that !")
                speakengine.runAndWait()
                eel.readyState()
                rsuccess2()
            else:
                eel.set_appstatus(3)
                speakengine.say("Sorry I couldn't understand please try again !")
                speakengine.runAndWait()
                eel.startListening2()
except Exception:
        frontend_engine = pw.getWindowsWithTitle('Jessica')[0]
        frontend_engine.restore()
        eel.set_appstatus(4)
        speakengine.say("An error occured while carrying out skills function please check the scripts for error !!")
        speakengine.runAndWait()
        eel.readyState()
