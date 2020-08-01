import os
import webbrowser
def hello():
        print('Jiiiiiiiiii')
hello()
import webbrowser    
urL='file:///P:/01/backend_engine/frontend_engine/index.html'
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(urL)
cwd = os.getcwd()   
      
# Print the current working    
# directory (CWD)   
print("Current working directory:") 
print(cwd + "\\frontend_engine")