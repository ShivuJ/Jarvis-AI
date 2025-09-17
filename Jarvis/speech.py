import json

import pyttsx3
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init()

print("Available Microphones: ")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(index, name)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.3)
        print("Using mic:", sr.Microphone.list_microphone_names()[source.device_index])

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            # data = json.loads(result)
            # query = data.get("text", data)
            speak("You said" + query)

        except Exception as e:
            print(e)
            speak("Say that again please...")
            return "None"

    return query