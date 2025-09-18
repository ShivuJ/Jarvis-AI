from speech import take_command, speak
import commands

if __name__ == "__main__":
    commands.wish()
    speak("Welcome back, How can I assist you?")

    while True:
        query = take_command().lower()

        if "date" in query:
            commands.date()

        elif "time" in query:
            commands.time()

        elif "search" in query:
            commands.search(query)