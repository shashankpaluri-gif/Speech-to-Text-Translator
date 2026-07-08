!pip install SpeechRecognition
!pip install googletrans==4.0.0-rc1
from google.colab import files

uploaded = files.upload()
import speech_recognition as sr
from googletrans import Translator

recognizer = sr.Recognizer()

with sr.AudioFile("record.wav") as source:
    audio = recognizer.record(source)

text = recognizer.recognize_google(audio)

print("You said:", text)

translator = Translator()
translated = translator.translate(text, dest="te")

print("Translated:", translated.text)
