import pyttsx3
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    speak("Welcome back, How may I help you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_vosk(audio, language="en")
            speak("You said" + query)

        except Exception as e:
            print(e)
            speak("Say that again please...")
            return "None"

    return query



if __name__ == "__main__":
    wish()
    while True:
        query = take_command().lower()
    # speak("You said: " + query)