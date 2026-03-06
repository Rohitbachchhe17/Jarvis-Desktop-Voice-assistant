import pyttsx3
import os
import time
import webbrowser
from reportlab.pdfgen import canvas

def speak(text):
    print("Jarvis:", text)
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.2)

speak("Jarvis activated")

while True:
    command = input("Type command: ").lower()

    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open whatsapp" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "open command prompt" in command:
        speak("Opening Command Prompt")
        os.system("start cmd")

    elif "open settings" in command:
        speak("Opening Windows Settings")
        os.system("start ms-settings:")

    elif "open file manager" in command:
        speak("Opening File Explorer")
        os.system("explorer")

    elif "make pdf" in command:
        speak("Creating PDF")
        c = canvas.Canvas("jarvis_created.pdf")
        c.drawString(100, 750, "PDF created by Jarvis")
        c.save()
        speak("PDF created successfully")

    elif "stop jarvis" in command:
        speak("Goodbye")
        break

    else:
        speak("Sorry, I did not understand that command")
