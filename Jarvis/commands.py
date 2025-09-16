import datetime

from speech import speak

def date():
    dateNow = datetime.datetime.now()
    speak(f"The current date is {dateNow}")

def wish():
    speak("Welcome back, How may I help you?")