import speech_recognition as sr
#import webbrowser as web
import os
import pyaudio

r1 = sr.Recognizer()
r2 = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        audio = r1.listen(source)
        print(r2.recognize_google(audio))
