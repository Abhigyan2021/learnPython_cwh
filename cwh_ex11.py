
# Sending Notification for Water Breaks

import win32com.client as wincom
import time

speak = wincom.Dispatch("SAPI.SpVoice")

text = "Abhigyan Please Take a Water Break!!"

i = 0

while (True):

    if i == 4:
        break

    speak.Speak(text)
    time.sleep(5)

    i = i + 1