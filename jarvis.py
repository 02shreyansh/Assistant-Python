import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from  requests import get
import wikipedia
import webbrowser
import pywhatkit as kit 
import smtplib
import sys

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)
#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
# convert voice to text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        audio= r.listen(source,timeout=1,phrase_time_limit=5)


    try:
        print("Recognizing....")
        query= r.recognize_google(audio,language='en-in')
        print(f"user said : {query}")
    except Exception as e:
        speak("Say that again Please..")
        return "none"
    return query

#to wish
def wish():
    hour=int(datetime.datetime.now().hour)  #exact time
    if( hour>=0 and hour<=12):
        speak("Good Morning")
    elif (hour>12 and hour<17):
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am AI ,Please tell me how can i help you?")


def SendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','password')
    server.sendmail('email id',to,content)
    server.close()
  

if __name__== "__main__":
    wish()
    
    
    while True:
        query = takecommand().lower()

        #logic buliding for task

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        
        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
        elif "wikipedia" in query:
            speak("searching Wikipedia")
            query=query.replace("wikipedia" ,"")
            results=wikipedia.summary(query,sentences=50)
            speak("according to wikipedia")
            speak(results)
        elif "open youtube" in query:
            url='https://www.youtube.com/'
            webbrowser.open(url)
        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")
        elif "open google" in query:
            speak("what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+917982702178", "Hello!",2,24) # 2 24 means time
        elif "play song on youtube" in query:
            kit.playonyt("see you again")
        elif "email to shreyansh" in query:
            try:
                speak("what should i say")
                content =takecommand().lower()
                to= "02.shreyansh.10@gmail.com"
                SendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry sir,I am not able to send email")
        
        elif "no thanks" in query:
            speak("Thanks for using me sir,have a nice day sir")
            sys.exit()
        speak("sir,do you have any other work")


            
            
            
        





    
    