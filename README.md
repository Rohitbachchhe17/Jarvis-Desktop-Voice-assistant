# 🤖 Jarvis Desktop Assistant (Python)

A simple **Python-based desktop assistant** inspired by Jarvis.
This assistant can open websites, launch system applications, and generate PDF files using simple commands.

The project uses **Text-to-Speech (TTS)** so the assistant responds like a virtual AI assistant.

---

# 🚀 Features

* 🔊 Text-to-Speech responses
* 🌐 Open websites like YouTube, Google, and WhatsApp
* 🖥 Open system applications (Notepad, Calculator, CMD)
* ⚙ Open Windows Settings
* 📂 Open File Explorer
* 📄 Generate PDF files automatically
* ⌨ Command-based interaction

---

# 🛠 Technologies Used

* Python
* pyttsx3 (Text-to-Speech)
* webbrowser
* os
* time
* reportlab (PDF Generation)

---

# 📦 Installation

Install the required libraries before running the project.

```bash
pip install pyttsx3
pip install reportlab
```

---

# 📂 Project Structure

```
jarvis-assistant/
│
├── jarvis.py
├── jarvis_created.pdf
└── README.md
```

---

# 📜 Code Overview

### Import Libraries

```python
import pyttsx3
import os
import time
import webbrowser
from reportlab.pdfgen import canvas
```

These libraries help in speech generation, opening applications, and creating PDF files.

---

### Speak Function

```python
def speak(text):
    print("Jarvis:", text)
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.2)
```

This function converts text into speech and prints the response on the screen.

---

### Activate Jarvis

```python
speak("Jarvis activated")
```

This line announces that the assistant has started.

---

### Command Loop

```python
while True:
```

Jarvis runs continuously and waits for user commands until it is stopped.

---

### User Command Input

```python
command = input("Type command: ").lower()
```

The user types a command, and it is converted to lowercase for easier processing.

---

# 🌐 Supported Commands

### Open YouTube

```python
elif "open youtube" in command:
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")
```

---

### Open Google

```python
elif "open google" in command:
    speak("Opening Google")
    webbrowser.open("https://www.google.com")
```

---

### Open WhatsApp Web

```python
elif "open whatsapp" in command:
    speak("Opening WhatsApp")
    webbrowser.open("https://web.whatsapp.com")
```

---

# 🖥 Open System Applications

### Notepad

```python
os.system("notepad")
```

### Calculator

```python
os.system("calc")
```

### Command Prompt

```python
os.system("start cmd")
```

---

# ⚙ Open Windows Settings

```python
os.system("start ms-settings:")
```

---

# 📂 Open File Explorer

```python
os.system("explorer")
```

---

# 📄 Generate PDF File

```python
elif "make pdf" in command:
    speak("Creating PDF")
    c = canvas.Canvas("jarvis_created.pdf")
    c.drawString(100, 750, "PDF created by Jarvis")
    c.save()
```

This creates a PDF file named:

```
jarvis_created.pdf
```

---

# 🛑 Stop Jarvis

```python
elif "stop jarvis" in command:
    speak("Goodbye")
    break
```

This command stops the assistant.

---

# ▶ How to Run the Project

Clone the repository

```bash
git clone https://github.com/yourusername/jarvis-desktop-assistant
```

Go to the project folder

```bash
cd jarvis-desktop-assistant
```

Run the Python script

```bash
python jarvis.py
```

---

# 💡 Example Commands

```
open youtube
open google
open whatsapp
open notepad
open calculator
open command prompt
open settings
open file manager
make pdf
stop jarvis
```

---

# 🔮 Future Improvements

* 🎤 Voice recognition using SpeechRecognition
* 🤖 AI chatbot integration
* 🌦 Weather updates
* 📅 Task reminders
* 🎵 Music control
* 📰 News updates

---

# 👨‍💻 Author

**Saurav Kumavat**

📧 Email: [rohitbachchhe17@gmail.com](mailto:rohitbachchhe17@gmail.com)
📍 India

---

⭐ If you like this project, consider giving it a star on GitHub.
