import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()




def speak(audio):
    engine.say(audio)
    engine.runAndWait( )

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    

def date():
    year = int(datetime.datetime.now().year)
    month =int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    

def wisher():
    speak("welcome back ajay")
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning sir")
    elif hour >=12 and hour<18:
        speak("good afternoon sir")
    elif hour >=18 and hour<24:
        speak("good evening sir")
    else:
        speak("good night sir")

    
    date()
    
    time()
   
    
    speak("Your Shadow at your service. how can i help u")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print("Recongnizning....")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("say that again please....")

        return "None"
    return query

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ajayramlvr@gmail.com','Iamajayram@123')#username and password
    server.sendmail('ajayramlvr@gmail.com',to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\saves\screenshots\ss.sv.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent )

def jokes():
    speak(pyjokes.get_joke())
if __name__ == "__main__":
    wisher()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikepedia","")
            result = wikipedia.summary(query, sentence+2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = 'ultrashadow12345@gmail.com'
                sendmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
        elif 'search in chrome' in query:
            speak("what should i search ?")
            chromepath = 'C:\Program Files (x86)\CryptoTab Browser\Application\browser.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
        
        elif 'logout' in query:
            os.system("shutdown -1")

        elif 'shudown' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
            os.system("shudown /r /t 1")
        
        elif 'play some music' in query:
            songs_dir = 'D:\audios'
            songs = os.listdir(songs_dir)
            os.startfile(os.path(songs_dir, songs[0]))

        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            remember= open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you anything' in query:
            remember = opem('data.txt', 'r')
            speak("you said me to remember that " +remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("done!")
        
        elif 'cpu' in query:
            cpu()
        elif 'jokes' in query:
            jokes()
        elif 'time' in query:
            speak("the current time is ")
            speak(time)
        elif 'date' in query:
            speak("the current date is ")
            speak(date)
            speak(month)
            speak(year)
        elif 'offline' in query:
            quit()