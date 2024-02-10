import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import pyjokes
from  requests import get
import wikipedia
import webbrowser
import pywhatkit as kit 
import smtplib


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

#send email
def SendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','password')
    server.sendmail('email id',to,content)
    server.close()
  
#function to run
def run_jarvis():
    
    query = takecommand().lower()

#logic buliding for task
    # open notepad
    if "open notepad" in query:
        npath = "C:\\Windows\\system32\\notepad.exe"
        os.startfile(npath)
    #for hello and hi
    elif "hello" in query or "yo" in query:
        speak("hello,How are you")
    
    #open cmd
        
    elif "open command prompt" in query:
        os.system("start cmd")
    
    #open camera
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
    #ip address
        
    elif "ip address" in query:
        ip=get('https://api.ipify.org').text
        speak(f"your IP address is {ip}")

    #wikipedia
    elif "wikipedia" in query:
        speak("searching Wikipedia")
        query=query.replace("wikipedia" ,"")
        results=wikipedia.summary(query,sentences=50)
        speak("according to wikipedia")
        speak(results)
    
    #open youtube

    elif "open youtube" in query:
        url='https://www.youtube.com/'
        webbrowser.open(url)

    #open stack Overflow
    elif "open stack overflow" in query:
        webbrowser.open("www.stackoverflow.com")
    # open google
    elif "open google" in query:
        speak("what should i search on google")
        cm=takecommand().lower()
        webbrowser.open(f"{cm}")
    # send whatsaap msg
    elif "send message" in query:
        kit.sendwhatmsg("+917982702178", "Hello!",2,24) # 2 24 means time
    # play music
    elif "play" in query:
        song =query.replace("play","")
        speak("playing" + song)
        kit.playonyt(song)
    # tell time
    elif "time" in query:
        time=datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        speak("current time is " + time)
    
    # send email
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
    #tell joke
    elif "joke" in query:
        speak(pyjokes.get_joke())
    # for exit    
    elif "no thanks" in query or "exit" in query:
        speak("Thanks for using me sir,have a nice day sir")
        exit()

    # when all statement false
    else:
        speak("i haven't understand,do you have any other work")

# for wish        
wish()  
# to run continue 
while True:
    run_jarvis()


            
            
            
        





    
    