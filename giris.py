import speech_recognition as sr
import os
import time
from gtts import gTTS
from gtts import *
from speak import *
from playsound import playsound
from veri import *
playsound("start.mp3")
speak("Ben Roku, hizmetinizdeyim")
def giris():
    r = sr.Recognizer()
    while(True):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("GİRİŞ BEKLENİYOR.")
                audio = r.listen(source)
                data = ""
                data = r.recognize_google(audio)
                data=data.lower()
                print("Bunu Söyledin :" + data)
                if data in rokugiris:
                    playsound("beep.mp3")
                    print("Giriş BAŞARILI")
                    break
                else:
                    continue
        except sr.UnknownValueError:
                print("GİRİŞ ALINAMADI!")
                continue
