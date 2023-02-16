import pyttsx3
import datetime
import math
from time import sleep 
import speech_recognition as sr 
import wikipedia
import webbrowser as wb
import os
import requests
import pyautogui
from pyautogui import click
import pyjokes
from os import name, startfile
from keyboard import press
from keyboard import write
from keyboard import press_and_release
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
rate = 190
engine.setProperty('rate', rate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    hour = datetime.datetime.now().hour
    if hour > 24 and hour < 12:
        speak("now the time is")
        speak(Time)
        speak("a,m")
    else:
        speak("now the time is")
        speak(Time)
        speak("p,m")
def date():
    date = int(datetime.datetime.now().day)
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    speak("now the date is")
    speak(date)
    speak(month)
    speak(year)
def whatsappmsg(name,message):
    os.startfile("C://Users//sbmur//AppData//Local//WhatsApp//WhatsApp.exe")
    sleep(8)
    click(x=192, y=165)
    write(name)
    sleep(4)
    click(x=191, y=315)
    sleep(3)
    write(message)
    sleep(2)
    press_and_release('enter') 
def wishme():
    hour = datetime.datetime.now().hour
    if hour > 0 and hour <= 11 :
        speak("GOOD MORNING SIR")
    elif hour > 11 and hour <= 16 :
        speak("good afternoon sir")
    elif hour> 16 and hour <=19 :
        speak (" good evening sir")
    else :
        speak("good night sir")   
def screen():
    img = pyautogui.screenshot()
    img.save("C://Users//sbmur//Pictures//Screenshots//ss.png")
def joke():
    j = pyjokes.get_joke()
    print(j)
    speak(j)
def quadratic():
    speak("give the values of a,b and c")
    print("In the format ax^2 + b x + c = 0")
    a = float(input("TYPE THE VALUE OF a:"))
    b = float(input("TYPE THE VALUE OF b:"))
    c = float(input("TYPE THE VALUE OF c:"))
    ac4 = 4*a*c
    bsqr = b*b
    d = bsqr - ac4
    x1 = (-1*b + math.sqrt(d))/2*a
    x2 = (-1*b - math.sqrt(d))/2*a
    print("The roots of the given quadratic equation are",x1,"and",x2)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source,duration=1) 
        print("Listening sir...........")
        audio = r.listen(source)
        try:
            print("Recognizing sir.......")
            query = r.recognize_google(audio,language='en-US')
            print(query)
        except Exception as e:
            print("Please say that again Sir")
            return "None"
    return(query)
if  __name__ == "__main__":
    speak("hello master this is jarvis")
    wishme()
    speak("how may i help you sir")
    while True:
          query= takeCommand().lower() 
          if "time" in query:
                time()
          elif "date" in query:
                date()
          elif "like me" in query:
              print("Yes Sir I like you to be more precise not only you but also all the human beings")
              speak("Yes Sir I like you to be more precise not only you but also all the human beings")
          elif "quadratic equation" in query:
                 quadratic()
          elif "how are you" in query:
              print("yes sir i am fine how about you?")
              speak("yes sir I am fine how about you?")
              reply = takeCommand().lower()
              if "fine" in reply:
                  print("I am so happy to hear that Sir, Tell me Sir how may I help you?")
                  speak("I am so happy to hear that Sir, Tell me Sir how may I help you?")
          elif "wikipedia" in query:
              print("searching Sir")
              speak("searching Sir")
              query= query.replace("wikipedia", "")
              result=wikipedia.summary(query, sentences=2)
              print(result)
              speak(result)
          elif "open whatsapp" in query:
               name = input("enter the name:")
               speak(" tell me the message sir")
               content = takeCommand() 
               whatsappmsg(name,content) 
          elif "where am i" in query:
               speak("wait sir, let me check")
               try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url ='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    country = geo_data['country']
                    city = geo_data['city']
                    region = geo_data['region']
                    print("Country:",country)
                    print("State:",region)
                    print("City:",city)
               except Exception as e:
                    print(e)
                    print("Sorry sir, due to network issue iam not able to find where you are")
                    speak 
          elif "google" in query:
              speak("opening chrome sir")
              os.startfile("C://Program Files//Google//Chrome//Application//chrome.exe")
          elif "youtube" in query:
               speak("opening youtube sir")
               os.startfile("C://Program Files//Google//Chrome//Application//chrome.exe")
               sleep(1)
               click(x=582, y=802)
          elif "search in chrome" in query:
               speak("what should i search")
               search = takeCommand()
               os.startfile("C://Program Files//Google//Chrome//Application//chrome.exe")
               sleep(1)
               click(x=700, y=614)
               sleep(0.5)
               write(search)
               press_and_release('enter')
          elif "shutdown" in query:
              os.system("shutdown /s /t 1")
              quit()
          elif "restart" in query:
              os.system("shutdown /r /t 1")
              quit()
          elif "firefox" in query:
               speak("opening Firefox Sir")
               os.startfile("C://Program Files//Mozilla Firefox//firefox.exe")
          elif "play songs" in query:
               songs_dir="C://Users//sbmur//Music//Video Projects"
               songs=os.listdir(songs_dir)
               os.startfile(os.path.join(songs_dir,songs[0]))
          elif "offline" in query:
              speak("Thank you sir, iam leaving right now you can call me by saying activate jarvis ")
              quit()
          elif "do you know anything" in query:
              remember = open("data1.txt",'r')
              speak("you said me to remember that" + remember.read())
          elif "remember" in query:
              speak("what should i remember sir?")
              data = takeCommand()
              speak("you said me to remember that" + data)
              remember = open("data1.txt",'w')
              remember.write(data)
              remember.close()
          elif "add command" in query:
              print("Thank you for adding commands sir, This makes me smarter and smarter")
              os.startfile("C://Users//sbmur//Desktop//jarvis03//jarvis03.py")
          elif "joke" in query:
              joke()
          elif "open classroom" in query:
              speak("opening clasroom sir")
              os.startfile("C://Program Files//Google//Chrome//Application//chrome.exe")
              sleep(1)
              click(x=700, y=614)
              sleep(0.5)
              write("https://classroom.google.com/u/0/h")
              press_and_release('enter')
          elif "your commands" in query:
              os.startfile("D://jarvis03 commands.txt")
          elif "d drive" in query:
              os.startfile("D://")
          elif "c drive" in query:
              os.startfile("C://")
          elif "screenshot" in query:
              speak("taking Screenshot Sir")
              screen()
          elif "open basic electrical notes" in query:
              os.startfile("D://BE8254 notes.pdf")
