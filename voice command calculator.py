import speech_recognition as sr
import pyttsx3
import re

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the speaker
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Error occurred while speaking:", e)

# Function to listen to the command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an error recognizing the audio.")
            return ""

# Function to calculate the result
def calculate(text):
    numbers = re.findall(r'\d+', text)
    if len(numbers) != 2:
        return "Sorry, I couldn't recognize the numbers."
    num1, num2 = map(int, numbers)
    if '+' in text:
        result = num1 + num2
    elif '-' in text:
        result = num1 - num2
    elif '*' in text:
        result = num1 * num2
    elif '/' in text:
        if num2 == 0:
            return "Cannot divide by zero."
        result = num1 / num2
    else:
        result = "Sorry, I can't perform this operation."
    return result

# Main function
def main():
    try:
        speak("Welcome to the voice command calculator. Please say a command.")
        command = listen()
        if command:
            result = calculate(command)
            speak(f"The result is {result}")
    except Exception as e:
        print("An error occurred:", e)

# Call the main function
main()
