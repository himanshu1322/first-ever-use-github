# -*- coding: utf-8 -*-
"""
Created on Sun May  3 21:54:02 2020

@author: SONY LAPTOP
"""
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 130)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def subhkamna():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning')
    elif hour> 12 and hour< 18:
        speak('good afternoon ')
    else:
        speak('good evening')
    speak('i am rupali and my owner is himanshu how i help you')

def takecommand():
    #to take input from users
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("recognizing.....")
        query  = r.recognize_google(audio,language='en-in')
        print ( "users said:", query) 
    except Exception as e:
        print(e)
        print("say that again please.... ")
        return 'none'
    return query
     
if __name__ == "__main__":
    subhkamna()
    while True:
        query=takecommand().lower()
        if "wikipedia" in query :
            speak("searching wikipedia")
            query=query.replace("wikipedia"," ")
            results=  wikipedia.summary(query,sentences=4)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif "play music" in query:
            music_dir = 'E:\\himans'
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[0]))
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")
            speak("sir the time is ")
            speak(strTime)
           

            
            