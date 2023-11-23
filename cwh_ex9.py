
'''
Write a program to pronounce list of names using win32 API.
If you are given a list l as follows:
l = ["Rahul", "Nishant", "Harry"]

Your program should pronounce:
Shoutout to Rahul 
Shoutout to Nishant
Shoutout to Harry

'''

# Code of Solution():

import win32com.client as wincom
import time

speak = wincom.Dispatch("SAPI.SpVoice")

names = ["Rahul", "Modi", "Tharoor", "Kharge", "Nadda", "Shah" ]

for name in names :
    text = f"Shoutout to {name}"
    speak.Speak(text)

speak.Speak("You all did well.")