from speech import take_command, speak
import commands

if __name__ == "__main__":
    commands.wish()

    while True:
        query = take_command().lower()

        if "date" in query:
            commands.date()

        elif "time" in query:
            commands.time()