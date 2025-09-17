import datetime

from speech import speak

def date():
    datetoday = datetime.date.today()
    formatted_date = datetoday.strftime("%B %d, %Y")
    speak(f"The current date is {formatted_date}")

def wish():
    speak("Welcome back, How may I help you?")