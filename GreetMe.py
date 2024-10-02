import pyttsx3
import datetime

engine =  pyttsx3.init("sapi5") # object to control the speech engine
voices = engine.getProperty("voices") # method to get details of all voices available with the engine
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate", 300)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour <12:
        speak("Good morning!, Sir")
    elif hour > 12 and hour <= 18:
        speak("Good afternoon, Sir!")
    else:
        speak("Good evening, Sir.")

    speak("Please tell me, how can I help you ?")