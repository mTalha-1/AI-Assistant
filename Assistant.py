import pyttsx3
import datetime
import speech_recognition as sr


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

    speak("I am your AI assistant, my name is Loki. I will perform different tasks for you. Now tell me how may I help you.")
def voice_commands_to_text():
    rec_class = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning.....")
        rec_class.pause_threshold = 1
        audio = rec_class.listen(source)
    try:
        command = rec_class.recognize_google(audio,language='en-in')
        print("User said: ",audio,"\n" )
    except Exception as e:
        print(e)
        print("Please say your command again!")
        return "None"
    return command

if __name__ == "__main__":
    greeting()
    voice_commands_to_text()