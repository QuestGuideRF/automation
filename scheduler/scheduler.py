import schedule
import webbrowser
import os
import sys
import ctypes
import time
from playsound import playsound
def run ():
    print ('Запуск планировщика...')
def certain_show ():
    playsound ('sound.wav')
    print ('Шоу... идет!')
def open_email ():
    print ('Открытие электронной почты..')
    webbrowser .open (your_email )
def shutdown ():
    if sys .platform =='win32':
        user32 =ctypes .WinDLL ('user32')
        user32 .ExitWindowsEx (0x00000008 ,0x00000000 )
    else :
        os .system ('sudo выключится сейчас')
schedule .every ().monday .at ("20:00").do (certain_show )
schedule .every ().tuesday .at ("20:00").do (certain_show )
schedule .every (30 ).minutes .do (run )
schedule .every ().day .at ("08:00").do (open_email )
schedule .every ().day .at ("23:00").do (shutdown )
while True :
    schedule .run_pending ()
    time .sleep (1 )