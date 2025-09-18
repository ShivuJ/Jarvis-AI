import datetime
import wikipedia

from speech import speak

def date():
    datetoday = datetime.date.today()
    formatted_date = datetoday.strftime("%B %d, %Y")
    speak(f"The current date is {formatted_date}")

def time():
    timenow = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {timenow}")

def wish():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour < 21:
        speak("Good evening")
    else:
        speak("Good night")

def search(query):
    speak("Searching...")
    query = query.replace("search ", "")
    results = wikipedia.summary(query, sentences=5)
    speak("According to Wikipedia" + results)

