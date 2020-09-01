import pyttsx3
import speech_recognition as sr


def say(text, rate=150, voice='M', volume=1.0):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    voices = engine.getProperty('voices')
    if voice.upper() == 'M':
        i = 0
    elif voice.upper() == 'F':
        i = 1
    else:
        i = 0
    engine.setProperty('voice', voices[i].id)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            text = recognizer.record(audio)
            return text
        except:
            say("Sorry cant recognize your voice!")
