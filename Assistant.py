import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    present_hour = int(datetime.datetime.now().hour)

    if (present_hour>=4 and present_hour <12):
        speak("Good Morning!")
    elif(present_hour>=12 and present_hour <18):
        speak("Good Afternoon!") 
    elif(present_hour>=18 and present_hour<21):
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("I am your AI assistant, my name is Jarvis. I will perform different tasks for you. Now tell me how may I help you.")

def voice_commands_to_text():
    rec_class = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning.....")
        rec_class.pause_threshold = 0.5
        rec_class.energy_threshold = 450
        audio = rec_class.listen(source)
    try:
        print("Recognizing")
        command = rec_class.recognize_google(audio,language ='en-in')
        print("User said: ",command,"\n" )
    except Exception as e:
        print(e)
        print("Please say your command again!")
        return "None"
    return command


if __name__ == "__main__":
    greeting()
    while True:
        command  = voice_commands_to_text().lower()
        if 'wikipedia' in command:
            speak('Searching wikipedia')
            command = command.replace('wikipedia','')
            results = wikipedia.summary(command, sentences = 2)
            speak('According to wikipedia!')
            print(results)
            speak(results)
        elif 'open google' in command:
            webbrowser.open('google.com')

        elif 'open youtube ' in command:
            webbrowser.open('https://www.youtube.com/')

        elif 'in youtube' in command:
            se = command.split(' in ')[0]
            webbrowser.open(f'https://www.youtube.com/results?search_query={se}')

        elif 'current time' in command:
            speak("The time is" + datetime.datetime.now().strftime('%H:%M:%S'))
        
        elif 'open code' in command:
            Path = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(Path)