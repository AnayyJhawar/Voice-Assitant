import pyttsx3
import speech_recognition as speech
import datetime
import os
import cv2
import random
import webbrowser
from requests import get
import wikipedia

while_loop_creation=0

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    recog = speech.Recognizer()
    with speech.Microphone() as source:
        print("Listening...")
        recog.pause_threshold = 1
        audio = recog.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Validating...")
        query = recog.recognize_google(audio, language='en-us')
        print(f"You: {query}")

    except Exception as a:
        speak("I Couldn't Exactly Understand What You Were Speaking, Please Repeat")
        return "none"
    return query

def wishing_user():
    time_ = int(datetime.datetime.now().hour)
    if time_>0 and time_<12:
        speak("Good Morning Sir, I Am Techie, What Would You Like To Do Today?")

    elif time_>=12 and time_<18:
        speak("Good Afternoon Sir, I Am Techie, What Would You Like To Do Today?")

    else:
        speak("Good Evening Sir, I Am Techie, What Would You Like To Do Today?")

if __name__=="__main__":
    wishing_user()
    while True:
        query = takecommand().lower()
        if "notepad" in query:
            speak("Opening Notepad")
            directory = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(directory)

        elif "camera" in query:
            speak("Opening Camera")
            cam = cv2.VideoCapture(0)
            while True:
                ret, img = cam.read()
                cv2.imshow('Webcam', img)
                b = cv2.waitKey(50)
                if b == 25:
                    break
            cam.release()
            cv2.destroyAllWindows()

        elif "music" in query:
            webbrowser.open('https://www.youtube.com/watch?v=Z5oRdbfA-ko&list=PLHDGY-XjbxHtQCnqVpMB-hf5Fjf_2UGJo')

        elif "command prompt" in query:
            speak("Opening Command Prompt")
            os.system('start cmd')

        elif "ip address" in query:
            ip_address = get('https://api.ipify.org').text
            speak(f"Your IP Address Is: ")
            print(ip_address)

        elif "songs" in query:
            webbrowser.open('https://www.youtube.com/watch?v=Z5oRdbfA-ko&list=PLHDGY-XjbxHtQCnqVpMB-hf5Fjf_2UGJo')

        elif "what" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According To The Results...")
            speak(result)

        elif "why" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According To The Results...")
            speak(result)

        elif "who" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According To The Results...")
            speak(result)

        elif "how" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According To The Results...")
            speak(result)

        elif "which" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According To The Results...")
            speak(result)

        elif "whom" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According To The Results...")
            speak(result)

        elif "whose" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According To The Results...")
            speak(result)

        elif "when" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According To The Results...")
            speak(result)

        elif "where" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According To The Results...")
            speak(result)

        elif "no" in query:
            speak("Have A Good Day!")
            break

        elif "pycharm" in query:
            speak("Opening Pycharm...")
            directory = "C:\\Program Files\\\JetBrains\\\PyCharm Community Edition 2021.2\\bin\\pycharm64.exe"
            os.startfile(directory)

        elif "ppt" in query:
            speak("Opening Power Point...")
            directory = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(directory)

        elif "word" in query:
            speak("Opening Word...")
            directory = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"

        else:
            speak("Here Are The Search Results...")
            webbrowser.open(f"{query}")

        speak("Do You Have Any Other Work?")