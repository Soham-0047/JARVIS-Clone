import pyttsx3
from decouple import config
from datetime import datetime
import requests
from utils import opening_text 
import speech_recognition as sr
from random import choice

from pprint import pprint


USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

engine.setProperty('rate',190)

engine.setProperty('volume',2.0)

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):

    engine.say(text)
    engine.runAndWait()


def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    elif (hour >= 19) and (hour < 24):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME} How may I assist you? Do you need help")
    speak(f"myself {BOTNAME} and I will destroy earth ha ha ha....")
    speak(f"Do you know math?")
    

def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        
        elif 'hello' in query:
            speak(f"Hello also for you")
        
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

if __name__ == '__main__':

        greet_user()
        while True:
            query = take_user_input().lower()
            print(query)  




'''recognizer = sr.Recognizer()

while True:

    try:

        with sr.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic,duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized{text}")
            
    except sr.UnknownValueError():

        recognizer = sr.Recognizer()

        continue
'''