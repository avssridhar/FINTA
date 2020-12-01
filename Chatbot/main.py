import speech_recognition as sr
import webbrowser
import time
import playsound
import os 
import random
from gtts import gTTS
from time import ctime
r=sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
           finata_speak(ask)
        audio=r.listen(source)
        voice_data=''
        try: 
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            finata_speak('Sorry,I did not get that')
        except sr.RequestError:
            finata_speak('Sorry,my speech servcie is down')
        return voice_data

def finata_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,1000000)
    audio_file='audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if "what is your name" in voice_data:
        finata_speak('I am your Personal assistant Finata')
    if "Time" in voice_data:
        finata_speak(ctime())
    if 'search' in voice_data:
        search=record_audio('What do you want to search for')
        url='https://google.com/search?q=' + search
        webbrowser.get().open(url)
        finata_speak('Here is what I found for' + ' ' + search)
    if 'location' in voice_data:
        location=record_audio('What is the location you need?')
        url='https://google.com/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        finata_speak('Here is the location you needed' + ' '+ search)
    if  'exit' in voice_data:
        exit()
    
    
time.sleep(1)
finata_speak('Hey How can I help you?')
while 1:
    voice_data=record_audio()
    respond(voice_data)