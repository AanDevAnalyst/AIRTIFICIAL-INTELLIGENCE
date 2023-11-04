import speech_recognition as sr
import webbrowser
import time
import playsound
import os
from time import ctime
import random
from gtts import gTTS


r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            cortana_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = Recogniser.recognize_google(audio)

        except sr.UnknownValueError:
            cortana_speak("Sorry I Didn't Get That")

        except sr.RequestError:
            cortana_speak('Sorry Speech Service Is Down')

        return voice_data


def cortana_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    Random = random.randint(1, 10000000)
    audio_file = 'audio-' + str(Random) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        cortana_speak('My Name Is Cortana')

    if 'who create you' in voice_data:
        cortana_speak('Professor Abduljabbar Adogu Nuhu')

    if 'what time is it' in voice_data:
        cortana_speak(ctime())

    if 'search' in voice_data:
        search = record_audio('What Do You Want To Search')
        url = 'https:google.com/search?q=' + search
        webbrowser.get().open(url)
        cortana_speak('Here Is What I Found about' + search)

    if 'find location' in voice_data:
        location = record_audio('What Is The Location')
        url = 'https:what3word' + location + '&amp;'
        webbrowser.get().open(url)
        cortana_speak('Here Is The Location You Ask For' + location)

    if 'exit' in voice_data:
        exit()

time.sleep(1)
cortana_speak('How Can I Help You')
while 1:
    voice_data = record_audio()
    respond(voice_data)
