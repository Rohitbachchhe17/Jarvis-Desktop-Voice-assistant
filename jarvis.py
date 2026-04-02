import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import time
import smtplib
import subprocess
import psutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from reportlab.pdfgen import canvas


# -------------------------------------------------------------
# GLOBAL SPEECH ENGINE
# -------------------------------------------------------------
engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# -------------------------------------------------------------
# LISTEN FUNCTION
# -------------------------------------------------------------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        cmd = r.recognize_google(audio, language="en-IN")
        print("You said:", cmd)
        return cmd.lower()

    except:
        speak("I didn't understand. Please say again.")
        return ""


# -------------------------------------------------------------
# PDF CREATION
# -------------------------------------------------------------
def create_pdf(name="Jarvis_Output.pdf"):
    speak("Creating PDF")
    c = canvas.Canvas(name)
    c.drawString(100, 750, "PDF Created by Jarvis AI")
    c.drawString(100, 720, "Your advanced personal assistant.")
    c.save()
    speak("PDF created successfully")


# -------------------------------------------------------------
# SEND EMAIL
# -------------------------------------------------------------
def send_email(to, subject, message):

    user_email = "your_email@gmail.com"
    user_password = "your_password"

    try:
        msg = MIMEMultipart()
        msg["From"] = user_email
        msg["To"] = to
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user_email, user_password)
        server.sendmail(user_email, to, msg.as_string())
        server.quit()

        speak("Email sent successfully")
    except Exception as e:
        speak("Error sending email")
        print(e)


# -------------------------------------------------------------
# PLAY MUSIC
# -------------------------------------------------------------
def play_music():
    music_path = "C:\\Users\\Public\\Music"
    files = os.listdir(music_path)
    if files:
        os.startfile(os.path.join(music_path, files[0]))
        speak("Playing music")
    else:
        speak("No music found")


# -------------------------------------------------------------
# SYSTEM CONTROLS
# -------------------------------------------------------------
def shutdown_system():
    speak("Shutting down the system")
    os.system("shutdown /s /t 1")

def restart_system():
    speak("Restarting system")
    os.system("shutdown /r /t 1")

def battery_status():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        speak(f"Battery level is {percent} percent")
    else:
        speak("Battery information not available")

def open_application(app_name):
    paths = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "vscode": r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "notepad": "notepad",
        "calculator": "calc"
    }

    if app_name in paths:
        speak(f"Opening {app_name}")
        os.system(paths[app_name])
    else:
        speak(f"I cannot find {app_name} on this device")


# -------------------------------------------------------------
# MAIN COMMAND PROCESSOR
# -------------------------------------------------------------
def run_command(command):

    # BASIC FUNCTIONS
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open whatsapp" in command:
        speak("Opening WhatsApp Web")
        webbrowser.open("https://web.whatsapp.com")

    elif "play music" in command:
        play_music()

    elif "make pdf" in command:
        create_pdf()

    # SYSTEM CONTROL
    elif "shutdown" in command:
        shutdown_system()

    elif "restart" in command:
        restart_system()

    elif "battery" in command:
        battery_status()

    # APPLICATIONS
    elif "open notepad" in command or "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "open chrome" in command:
        open_application("chrome")

    elif "open vs code" in command:
        open_application("vscode")

    # EMAIL
    elif "send email" in command:
        speak("Whom should I send to?")
        to = input("Enter email: ")
        speak("Subject?")
        subject = input("Enter subject: ")
        speak("Message?")
        message = input("Enter message: ")
        send_email(to, subject, message)

    # EXIT
    elif "stop jarvis" in command or "exit" in command:
        speak("Goodbye Rohit. Jarvis shutting down.")
        exit()

    else:
        speak("Sorry, I did not understand that.")


# -------------------------------------------------------------
# MAIN LOOP
# -------------------------------------------------------------
if __name__ == "__main__":
    speak("Advanced Jarvis Activated. How can I help you?")

    while True:
        print("\n--- Choose Input Mode ---")
        print("1. Speak")
        print("2. Type")
        print("3. Exit")

        mode = input("Select: ")

        if mode == "1":
            command = listen()
            if command:
                run_command(command)

        elif mode == "2":
            command = input("Type your command: ").lower()
            run_command(command)

        elif mode == "3":
            speak("Goodbye Rohit.")
            break

        else:
            speak("Invalid choice")
