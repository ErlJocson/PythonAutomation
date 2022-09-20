import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        speak(command)
except:
    print("Closing .....")
    speak("There was an error!")