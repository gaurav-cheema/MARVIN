# ------ future must be at the top
from __future__ import print_function
# ------

# ------ My Packages
import data_struct
import command_strings
# ------

# ------ Python packages
import os, sys
import time
import pyttsx3
import numpy as np
import speech_recognition as sr
# ------


# from module_imports import *

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


"""
NEAT IDEA: instead of the first word of the input being "execute" to execute a program,
    use "command: execute". this way we can tell the computer that we are giving it a command to run and that command is execute.
    This eliminates several other issues.
"""


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)
        # os.system('play -nq -t alsa synth {} sine {}'.format(0.5, 440))
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception: " + str(e))
        
    return said.lower()

data_struct.make_tree(command_strings.command_strs)
WAKE_WORD = "hey jarvis"
data_struct.check_tree("kill spotify")

while True:

    print("VISION is listening...")
    audioInput = get_audio()

    if audioInput.count(WAKE_WORD) > 0:
        # os.system('play -nq -t alsa synth {} sine {}'.format(0.5, 440))
        speak("How can I help")
        audioInput = get_audio()
        audioText = audioInput.split(' ')

        data_struct.check_tree(audioInput)       
        print(audioInput)

        # NOTE_STRS = ["make a note", "take note", "remember", "notepad"]
        # if audioText[0] in NOTE_STRS:
                

# Really cool stuff. The code below in this condition is only executed if this file is run directly. If the file is imported to another file, the code is not excuted. This helps if we only need the functions from this file in another file. so we can write tests under this condition; and they are only executed if this file is run directly.
# if __name__ == '__main__':
#     main()
#     service = google_calendar.authenticate_google_calendar()
#     google_calendar.get_google_calendar_events(5, service)

