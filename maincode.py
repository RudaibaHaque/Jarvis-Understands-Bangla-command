import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import time
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
translator=Translator()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")


def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)


    try :
        print("recognizing....") 
        query =r.recognize_google(audio,language ='bn')
        print(f"User said:{query}\n") 

    except sr.UnknownValueError:
        print("could not understand")
        print("say that again please....")
    except sr.RequestError:
        speak("say that again please")


    translated_text=translator.translate(query,src='bn',dest='en')
    out=translated_text.text
    print(out)
    time.sleep(5)
    speak('you said')
    engine.say(str(out))
    engine.runAndWait()
    return out

def trans(p):
    translated_text=translator.translate(p,src='en',dest='bn')
    out1=translated_text.text
    print(out1)
    speak(str(out1))
    #time.sleep(5)
    #engine.say(str(out1))
    #engine.runAndWait()

def sendEmail(to, content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    password= open("password.txt","r").read
    server.login('rudaiba.pust@gmail.com','password')
    server.sendmail('rudaiba.pust@gmail.com',to,content)
    server.close()


if __name__=='__main__':
   WishMe()
   while True:
       q=trans("HEllo medam! i am your Jarvis")
       out= takeCommand().lower()
       if 'wikipedia' in out:
        speak('Searching Wikipedia......')
        out = out.replace("wikipedia","")
        results= wikipedia.summary(out, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

       elif 'open youtube' in out:
         webbrowser.open("youtube.com")
         speak("medam you tube is opening")
       elif 'open google' in out:
         webbrowser.open("google.com")
         speak("medam google is opening")
       elif 'open stackoverflow' in out:
         webbrowser.open("stackoverflow.com")
         speak("medam stackoverflow is opening")


       elif'open music' in out:
        music_dir = 'D:\\songs'
        speak("medam your song play list is opening")
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))

  
       elif 'send email' in out:
        try:
            speak("what should i say?")
            content =takeCommand()
            to= "rudaiba.pust@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")

        except Exception as e:
            print(e)
            speak("sorry medaam.I am not able to send this email")
       elif'temperature' in out:
           search="Temperature in Rajshahi"
           url=f"https://www.google.com/search?q={search}"
           r= requests.get(url)
           data= BeautifulSoup(r.text,"html.parser")
           temp= data.find ("div",class_= "BNeawe").text
           speak(f"temp is {temp}")
        


       
      