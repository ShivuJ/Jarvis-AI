import json

import pyttsx3
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            result = r.recognize_google(audio, language="en-in")
            data = json.loads(result)
            query = data.get("text", data)
            speak("You said" + query)

        except Exception as e:
            print(e)
            speak("Say that again please...")
            return "None"

    return query