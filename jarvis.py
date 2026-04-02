import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import time
from reportlab.pdfgen import canvas


# --------------------------------------------------
# GLOBAL SPEECH ENGINE (NO RUN LOOP ERROR)
# --------------------------------------------------
engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    """Text to Speech"""
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# --------------------------------------------------
# VOICE LISTENER
# --------------------------------------------------
def listen():
    """Convert speech to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        cmd = r.recognize_google(audio, language="en-IN")
        print("You said:", cmd)
        return cmd.lower()

    except:
        speak("Sorry, can you repeat that?")
        return ""


# --------------------------------------------------
# CREATE PDF
# --------------------------------------------------
def create_pdf():
    speak("Creating PDF")
    c = canvas.Canvas("Jarvis_Output.pdf")
    c.drawString(100, 750, "PDF created by Jarvis AI")
    c.drawString(100, 720, "Your personal voice assistant")
    c.save()
    speak("PDF created successfully")


# --------------------------------------------------
# MAIN COMMAND HANDLER
# --------------------------------------------------
def run_command(command):

    # Web
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open whatsapp" in command:
        speak("Opening WhatsApp Web")
        webbrowser.open("https://web.whatsapp.com")

    # Apps
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "open file explorer" in command or "open file manager" in command:
        speak("Opening File Explorer")
        os.system("explorer")

    elif "open command prompt" in command:
        speak("Opening Command Prompt")
        os.system("start cmd")

    elif "open settings" in command:
        speak("Opening Windows Settings")
        os.system("start ms-settings:")

    # PDF
    elif "make pdf" in command or "create pdf" in command:
        create_pdf()

    # Exit
    elif "stop jarvis" in command or "quit" in command:
        speak("Goodbye Rohit. Jarvis shutting down.")
        exit()

    else:
        speak("Sorry Rohit, I did not understand that command.")


# --------------------------------------------------
# MAIN PROGRAM LOOP
# --------------------------------------------------
if __name__ == "__main__":
    speak("Jarvis Activated. How can I help you?")

    while True:
        print("\n----------------------")
        print("1. Speak")
        print("2. Type")
        print("3. Exit")
        print("----------------------")

        mode = input("Choose input method: ").strip()

        if mode == "1":
            command = listen()
            if command:
                run_command(command)

        elif mode == "2":
            command = input("Type command: ").lower()
            run_command(command)

        elif mode == "3":
            speak("Goodbye Rohit.")
            break

        else:
            print("Invalid choice!")
