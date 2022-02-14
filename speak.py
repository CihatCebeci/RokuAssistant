from gtts import gTTS
import os
from playsound import playsound
import random
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='tr')
    file1 = str("audio"+ str(random.random()) +".mp3")
    tts.save(file1)
    playsound(file1,True)
    os.remove(file1)
