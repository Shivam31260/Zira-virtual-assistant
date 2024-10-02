import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=5abdffb725714f1784268ca67c7cdb2d",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=5abdffb725714f1784268ca67c7cdb2d",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=5abdffb725714f1784268ca67c7cdb2d",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=5abdffb725714f1784268ca67c7cdb2d",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=5abdffb725714f1784268ca67c7cdb2d",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=5abdffb725714f1784268ca67c7cdb2d"}

    speak("Which field news do you want, [business], [health], [technology], [sports], [entertainment], [science]")
    field = input("Type the field of news you want: ")

    url = api_dict.get(field.lower())
    if not url:
        speak("Sorry, the requested category was not found.")
        return

    news = requests.get(url).json()
    speak("Here is the first news.")

    articles = news.get("articles", [])
    for article in articles:
        title = article.get("title")
        if title:
            print(title)
            speak(title)
            news_url = article.get("url")
            if news_url:
                print(f"For more info, visit: {news_url}")

            a = input("[Press 1 to continue] and [Press 2 to stop]")
            if a == "2":
                break

    speak("That's all.")
