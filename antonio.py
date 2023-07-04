import speech_recognition as sr
import pyttsx3
import datetime
from googlesearch import search
import requests
from bs4 import BeautifulSoup

# Initialize speech recognition
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# Jarvis responses
greetings = ['hello', 'hi', 'hey']
farewells = ['bye', 'goodbye']
time = ['what is the time', 'what"s the time']
capability = ["what can you do"]
location = ['where are you from']
weather = ["What's the weather like", "How's the weather today"]
age = ["how old are you", "what is your age"]
he_lp = ["help", "i need help", "can you help me", "what should I do"]
appreciation = ["thank you", "thanks", "thanks a lot", "i appreciate it"]
credit_score = ["what is a credit score", "how do I check my credit score", "how can I improve my credit score"]


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
        print("User:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        print("Sorry, I am currently unavailable.")
        return ""


# Function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Func
# tion to handle user commands
def handle_command(command):
    if command in greetings:
        speak("Hello Orlando!, how can I assist you?")
    elif command in farewells:
        speak("Goodbye!")
        return True
    elif command in time:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak("The current time is " + current_time)
    elif command in location:
        speak("I am from planet Mars")
    elif command in weather:
        speak("I'm sorry, I cannot provide real-time weather information.\n"
              "You can check the weather on a weather app or website.")
    elif command in capability:
        speak("For now, I am not capable of doing much, but\n"
              "in the near future, I'm going to be able to do better. "
              "But at least I can tell you my name, location, and my capabilities like I'm doing at the moment.")
    elif command in appreciation:
        speak("You're welcome! I'm glad I could help.")
    elif command in age:
        speak("I don't have an age. I'm a chatbot,\n"
              "I was born in the digital world. To me, age is just a number like 0s and 1s.")
    elif command in credit_score:
        speak("A credit score is a number that represents your creditworthiness.\n"
              "It is based on your credit history and is used by lenders to determine whether or not to lend you money.\n"
              "The higher your credit score, the more likely you are to be approved for credit.\n"
              "You can check your credit score for free on several websites such as Credit Karma and Credit Sesame.")
    else:
        speak("Searching Google for " + command)
        search_results = list(search(command))

        if len(search_results) > 0:
            speak("Here are some search results:")
            for i, result in enumerate(search_results, start=1):
                speak("Result " + str(i) + ": " + result)
                try:
                    response = requests.get(result)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    paragraphs = soup.find_all('p')
                    first_paragraph = paragraphs[0].text.strip() if paragraphs else "No description available."
                    speak("The first paragraph of the website is:")
                    speak(first_paragraph)
                except requests.RequestException:
                    speak("Sorry, I couldn't fetch the content of the website.")
        else:
            speak("Sorry, I couldn't find any relevant search results.")
            return False  # Continue the loop


while True:
    command = listen()
    if handle_command(command):
        break  # Exit the loop
