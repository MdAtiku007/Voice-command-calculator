# 🎙️ Voice Command Calculator

A simple **Voice Command Calculator** built with Python that allows users to perform basic arithmetic operations using their **voice commands**.

The application uses **Speech Recognition** to convert spoken commands into text and **Text-to-Speech (TTS)** to speak the calculated result back to the user.

---

## 📌 Project Overview

The Voice Command Calculator is a beginner-friendly Python project that combines:

* 🎤 Speech Recognition
* 🧮 Arithmetic Operations
* 🔊 Text-to-Speech
* 🐍 Python Programming
* 🔎 Regular Expressions

Instead of manually entering numbers using a keyboard, the user can speak a mathematical expression. The application processes the command, extracts the numbers, performs the requested calculation, and speaks the result.

---

## ✨ Features

* 🎤 **Voice Input** – Accepts commands through the microphone.
* 🧠 **Speech Recognition** – Converts speech into text using Google Speech Recognition.
* ➕ **Addition** – Performs addition of two numbers.
* ➖ **Subtraction** – Performs subtraction of two numbers.
* ✖️ **Multiplication** – Performs multiplication of two numbers.
* ➗ **Division** – Performs division of two numbers.
* 🚫 **Division by Zero Handling** – Prevents division by zero.
* 🔊 **Voice Output** – Speaks the calculated result.
* 🔎 **Number Extraction** – Uses Regular Expressions to identify numbers from the recognized text.
* ⚠️ **Error Handling** – Handles speech recognition and microphone-related errors.

---

## 🛠️ Technologies Used

| Technology                | Purpose                    |
| ------------------------- | -------------------------- |
| Python                    | Main programming language  |
| SpeechRecognition         | Converts speech into text  |
| Google Speech Recognition | Speech recognition service |
| PyAudio                   | Microphone/audio input     |
| pyttsx3                   | Text-to-Speech             |
| re                        | Extracts numbers from text |

---

## 📂 Project Structure

```text
Voice-Command-Calculator/
│
├── calculator.py
├── README.md

```

> Replace `calculator.py` with the actual filename of your Python file if it is different.

---

## ⚙️ How It Works

The application follows these basic steps:

```text
        Start
          ↓
 Initialize Speech Recognizer
          ↓
 Initialize Text-to-Speech Engine
          ↓
   Welcome Message
          ↓
   Listen Through Mic
          ↓
 Convert Speech → Text
          ↓
 Extract Two Numbers
          ↓
 Identify Operation
          ↓
 Perform Calculation
          ↓
   Speak the Result
          ↓
         End
```

---

## 🔄 Application Workflow

### 1. Initialize Speech Recognition

The program creates a speech recognizer using the `SpeechRecognition` library.

```python
r = sr.Recognizer()
```

This object is responsible for processing audio received from the microphone.

---

### 2. Initialize Text-to-Speech

The `pyttsx3` library is initialized to allow the computer to speak.

```python
engine = pyttsx3.init()
```

---

### 3. Speak Function

The `speak()` function converts text into spoken audio.

```python
def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Error occurred while speaking:", e)
```

---

### 4. Listen to User

The `listen()` function activates the microphone and records the user's voice.

```python
with sr.Microphone() as source:
    audio = r.listen(source)
```

The recorded audio is then sent to Google's speech recognition service:

```python
text = r.recognize_google(audio)
```

The recognized text is returned to the calculator.

---

### 5. Extract Numbers

The calculator uses Regular Expressions to find numbers in the recognized command.

```python
numbers = re.findall(r'\d+', text)
```

For example:

```text
Input: 25 + 10
Numbers detected: 25, 10
```

---

### 6. Perform Calculation

The program checks which operator is present in the recognized text.

```python
if '+' in text:
    result = num1 + num2
elif '-' in text:
    result = num1 - num2
elif '*' in text:
    result = num1 * num2
elif '/' in text:
    result = num1 / num2
```

---

### 7. Speak the Result

Finally, the result is spoken to the user.

```python
speak(f"The result is {result}")
```

For example:

```text
User: 25 + 10

Calculator:
The result is 35
```

---

# 🚀 Installation

## Prerequisites

Before running the project, make sure you have:

* Python 3.x
* Working microphone
* Internet connection
* Speaker/headphones

An internet connection is required because the current implementation uses Google's online speech recognition service.

---

## 1. Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Then move into the project folder:

```bash
cd Voice-Command-Calculator
```

---

## 2. Create a Virtual Environment

It is recommended to use a virtual environment.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install Required Libraries

Install the dependencies using:

```bash
pip install SpeechRecognition pyttsx3 PyAudio
```

Or, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

# 📦 requirements.txt

Create a file named:

```text
requirements.txt
```

and add:

```text
SpeechRecognition
pyttsx3
PyAudio
```

---

# ▶️ How to Run

Run the Python program using:

```bash
python calculator.py
```

You should hear:

```text
Welcome to the voice command calculator.
Please say a command.
```

Speak your mathematical expression into the microphone.

---

# 🎤 Example Commands

The current code is designed to recognize **two numerical values** and an arithmetic operator.

### Addition

```text
5 + 3
```

Output:

```text
The result is 8
```

### Subtraction

```text
10 - 4
```

Output:

```text
The result is 6
```

### Multiplication

```text
7 * 6
```

Output:

```text
The result is 42
```

### Division

```text
20 / 5
```

Output:

```text
The result is 4.0
```

### Division by Zero

```text
10 / 0
```

Output:

```text
Cannot divide by zero.
```

---

# 🧪 Example Execution

```text
Welcome to the voice command calculator. Please say a command.

Listening...

You said: 25 + 15

The result is 40
```

---

# 🧩 Main Functions

| Function      | Description                               |
| ------------- | ----------------------------------------- |
| `speak()`     | Converts text into speech                 |
| `listen()`    | Captures audio from microphone            |
| `calculate()` | Processes numbers and performs arithmetic |
| `main()`      | Controls the complete application         |

---

# 🔍 Error Handling

The project includes basic error handling for different situations.

### Speech Not Understood

If the speech cannot be recognized:

```text
Sorry, I could not understand what you said.
```

This is handled using:

```python
except sr.UnknownValueError:
```

### Speech Recognition Service Error

If there is a problem communicating with the speech recognition service:

```text
Sorry, there was an error recognizing the audio.
```

Handled using:

```python
except sr.RequestError:
```

### Invalid Number Input

If the program does not find exactly two numbers:

```text
Sorry, I couldn't recognize the numbers.
```

### Division by Zero

The program prevents division by zero:

```text
Cannot divide by zero.
```

---

# 🏗️ Project Architecture

```text
                 USER
                   │
                   ▼
             🎤 Microphone
                   │
                   ▼
        SpeechRecognition
                   │
                   ▼
             Spoken Text
                   │
                   ▼
          Regular Expression
           Number Extraction
                   │
                   ▼
          Operation Detection
                   │
                   ▼
          Calculation Function
                   │
                   ▼
               Result
                   │
                   ▼
             pyttsx3 TTS
                   │
                   ▼
             🔊 Voice Output
```

---

# 💡 Why This Project?

Traditional calculators require users to manually enter numbers and operators.

This project demonstrates how **voice interaction** can be integrated with a simple calculator to create a more natural user experience.

It also provides practical experience with:

* Python functions
* Exception handling
* Regular expressions
* Speech recognition
* Audio processing
* Text-to-speech
* External Python libraries

---

# 📚 Concepts Used

### Python Functions

The application is divided into separate functions such as:

```python
speak()
listen()
calculate()
main()
```

This makes the program easier to understand and maintain.

### Regular Expressions

The `re` module is used to extract numerical values:

```python
re.findall(r'\d+', text)
```

### Exception Handling

`try-except` blocks are used to prevent the application from crashing when errors occur.

### Conditional Statements

The program uses `if`, `elif`, and `else` to identify the arithmetic operation.

---

# ⚠️ Current Limitations

The current version is intentionally simple and has some limitations:

1. It works with **two numbers at a time**.
2. The current implementation extracts numerical digits using a regular expression.
3. It does not currently convert spoken number words such as `"five"` into `5`.
4. The operation is detected from symbols such as `+`, `-`, `*`, and `/`.
5. Speech recognition depends on Google's online recognition service.
6. An internet connection may be required for speech recognition.
7. Complex mathematical expressions are not currently supported.
8. The program performs one calculation and then exits.
9. It does not currently provide a graphical user interface.

---

# 🔮 Future Improvements

Several features can be added in future versions:

* 🗣️ Support commands such as **"five plus three"**
* 🔢 Support decimal numbers
* ➗ Support percentage calculations
* √ Add square root and power operations
* 🧮 Support multiple operations in one command
* 🔁 Continuous voice interaction
* 🖥️ Add a graphical user interface
* 📜 Add calculation history
* 🎨 Add a modern calculator interface
* 🌐 Support multiple languages
* 🎤 Improve speech recognition accuracy
* 🔊 Add customizable voice settings
* 📱 Create a web or mobile version
* 🤖 Add natural-language mathematical queries

---

# 🔐 Privacy Note

This project uses `recognize_google()` from the SpeechRecognition library for speech recognition.

Because the current implementation uses an online speech recognition service, users should be aware that audio processing may involve sending speech data to the external recognition service.

---

# 🛠️ Troubleshooting

## Microphone Not Detected

Make sure your microphone is connected and available to Python.

You can check available microphones using:

```python
import speech_recognition as sr

print(sr.Microphone.list_microphone_names())
```

---

## PyAudio Installation Error

If PyAudio fails to install on Windows, try:

```bash
pip install pipwin
pipwin install pyaudio
```

Alternatively, install a compatible PyAudio wheel for your Python version.

---

## Speech Recognition Not Working

Check:

* Microphone permissions
* Internet connection
* Microphone availability
* Python environment
* Required packages

---

## Speaker/Voice Output Not Working

Make sure your system has an available audio output device and that `pyttsx3` is installed correctly.

Try:

```bash
pip install pyttsx3
```

---

# 📈 Learning Outcomes

Through this project, I learned how to:

* Work with Python audio libraries
* Capture microphone input
* Convert speech into text
* Convert text into speech
* Extract information from text using Regular Expressions
* Perform arithmetic operations programmatically
* Handle runtime and recognition errors
* Structure a Python project using functions
* Work with external Python libraries

---

# 🎯 Use Cases

A voice-based calculator can be useful for:

* Hands-free calculations
* Accessibility-focused applications
* Voice assistant experiments
* Educational projects
* Python speech-processing projects
* Human-computer interaction experiments

---



```text
Voice-Command-Calculator/
│
├── calculator.py
├── README.md



# 📄 License

This project is available for educational and personal use.

You can add an open-source license such as the **MIT License** if you want others to freely use, modify, and distribute the project.

---

# 👨‍💻 Author

**MD Atiku Rahman**

B.Tech Computer Science Engineering
Galgotias University

### Connect With Me

* 💻 GitHub: [MdAtiku007](https://github.com/MdAtiku007)
* 🔗 LinkedIn: [Atiku Rahman](https://www.linkedin.com/in/atiku-rahman/)

---

# ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 🏷️ Tags

```text
python
voice-calculator
voice-command
speech-recognition
text-to-speech
python-project
calculator
speech-recognition-python
pyttsx3
pyaudio
google-speech-recognition
beginner-python-project
automation
voice-assistant
```
