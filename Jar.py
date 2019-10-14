##speech recognition

import speech_recognition as sr
import webbrowser as web
import os
import pyaudio

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[Search Google:Search Youtube]')
    print('Speak Now!')
    audio = r3.listen(source)
    print(audio)
    print(r2.recognize_google(audio))
if 'google' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url ="https://www.google.com/search?source=hp&ei=dvBzXdXuDNj2rQGXtpAg&q="
    with sr.Microphone() as source:
            print('What do you want to search!')
            audio = r2.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
                web.get().open_new(url+get)
            except sr.UnknownValueError:
                print('error')
            except sr.RequestError as e:
                print('failed'.format(e))
if 'video' in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url ="https://www.youtube.com/results?search_query="
    with sr.Microphone() as source:
            print('What do you want to search!')
            audio = r1.listen(source)
            try:
                get = r1.recognize_google(audio)
                print(get)
                web.get().open_new(url+get)
            except sr.UnknownValueError:
                print('error')
            except sr.RequestError as e:
                print('failed'.format(e))


# if 'notepad' in r2.recognize_google(audio):
#     os.system(notepad)
