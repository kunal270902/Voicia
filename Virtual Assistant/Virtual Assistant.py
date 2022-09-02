import random
import imdb
import pyttsx3      #pip install pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib        #pip install pipwin       #pipwin install pyaudio
import pywhatkit
import pyjokes
import googlesearch
import subprocess
import random
from tkinter import *
from tkinter import messagebox      #ETjX5Up6kuL8ew4ZqvSA0atrMzgOdNfBcYnPVK2lxb3ICoRJH1Gs7W9iQyhF


#GUI#
root = Tk()
root['bg'] = "black"
root.geometry("1024x768")
root.config(bg = "black")
root.title("Voicia Assistant")

icon = PhotoImage(file="C:\\Desktop\\img\\icon.png")
root.iconphoto(False, icon)

C = Canvas(root)
filename = PhotoImage(file = "C:\\Desktop\\img\\background.png")

background_label = Label(root, image=filename)
background_label.place(relx=0, rely=0)

C.pack()

name_label = Label(root, text="VOICIA VIRTUAL ASSISTANT", font=("Algerian", 40), anchor=W, foreground="#e75480", activeforeground="white", bg="#ffe5b4", activebackground="cyan")
name_label.place(x=75, y=5)

statusbar = Label(root, text='Welcome to Voicia', relief=SUNKEN, anchor=W, bg="cyan")
statusbar.pack(side=BOTTOM, fill=X)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(" Please tell me how may I help you")

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def exitProgram():
    quit()
def mainLoop():


    if __name__ == "__main__":
        wishMe()
        #while True:
        if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
    #Basic conversation

            elif'how are you' in query:
                speak('i am fine sir how are you')
            elif'thank you' in query:
                speak('my pleasure sir')
            elif'nice talking to you' in query:
                speak('thank you sir')



    #About me
            elif'yourself' in query:
                speak('i am a virtual assistant designed to help you')
            elif'creator' in query:
                speak('i was created by Kunal Awari')


    #webbrowser
            elif 'youtube' in query:
                speak("opening youtube")
                webbrowser.open("https://www.youtube.com/")

            elif 'google' in query:
                speak("opening google")
                webbrowser.open("https://www.google.com/")
            elif 'prime video' in query:
                speak("opening prime video")
                webbrowser.open("https://www.primevideo.com/?ref_=dvm_pds_amz_in_as_s_g_artemis_brand92|m_7V4epbApc_c442183710226")
            elif 'edx' in query:
                speak("opening e d x")
                webbrowser.open('https://enterprise.edx.org/dypeca')
            elif 'whatsapp' in query:
                speak("opening whatsapp")
                webbrowser.open('https://web.whatsapp.com/')
            elif'netflix' in query:
                speak("opening netflix")
                webbrowser.open("https://www.netflix.com/browse")
            elif 'spotify' in query:
                speak("opening spotify")
                webbrowser.open("https://open.spotify.com/")
            elif 'ms teams' in query:
                speak("opening ms teams")
                webbrowser.open("https://teams.microsoft.com/_#/pre-join-calling/19:a32a987514b34e23a357cd4f5e62b825@thread.tacv2")
            elif 'best stock' in query:
                webbrowser.open("https://www.moneycontrol.com/markets/stock-advice/")
            elif 'play game' in query:
                webbrowser.open('https://elgoog.im/t-rex/')


            #music os module
            elif 'play music' in query:
                music_dir = 'D:\\music'
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                print(songs)
                speak("playing ")
                os.startfile(os.path.join(music_dir, rd))
            elif 'play video in gaming' in query:
                music_dir = 'C:\\Videos\\VALORANT'
                video = os.listdir(music_dir)
                print(video)
                speak("playing ")
                os.startfile(os.path.join(music_dir, video[1]))
            elif 'play video in gta' in query:
                music_dir = 'C:\\videos\\GTA'
                video = os.listdir(music_dir)
                print(video)
                speak("playing ")
                os.startfile(os.path.join(music_dir, video[1]))
            elif 'play video in captures' in query:
                music_dir = 'C:\\Videos\\Captures'
                video = os.listdir(music_dir)
                print(video)
                speak("playing ")
                os.startfile(os.path.join(music_dir, video[1]))
            elif 'open certificates'  in query:
                music_dir = 'D:\\Certificates'
                video = os.listdir(music_dir)
                print(video)
                speak("opening")
                os.startfile(os.path.join(music_dir))
            elif 'chrome' in query:
                subprocess.call('C:\\Program Files\\Google\\Chrome\\Application')




    #datetime
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S:%A:%d:%B:%Y")
                speak(f"Sir, the time is {strTime}")



    #joke
            elif 'joke' in query:
                #print(pyjokes.get_joke())
                speak(pyjokes.get_joke())
                print(pyjokes.get_joke())
    #game

    #in youtube pywhatkit

            elif 'play' in query:
                song = query.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)

    #google
            elif 'search ' in query:
                question = query.replace('search', '')
                speak('searching ' + question)
                pywhatkit.search(question)

    #apps

            elif "open notepad" in query:
                speak('opening notepad')
                path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad'
                os.startfile(path)
            elif "open paint" in query:
                speak('opening paint')
                path='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint'
                os.startfile(path)
            #elif 'college notes' in query:
               # speak('which subject notes you want to open')


    #closing apps

            elif 'close notepad' in query:
                speak('closing notepad')
                os.system("taskkill /f /im notepad.exe")
            elif 'close paint' in query:
                speak('closing paint')
                os.system("taskkill /f /im Paint.exe")

   # imdb
            elif 'movie' in query:
                question = query.replace('movie','')
                ia=imdb.IMDb()
                search= ia.search_movie(question)
                speak('here are some movies')
                for i in search:
                    print(i)



    #stop
            elif 'stop' or 'quit' or 'exit' or 'close' in query:
                speak('quitting program')
                quit()


#GUI#

exit = Button(root, text="Exit", font=("Baskerville", 16), foreground="red", activeforeground="black", bg="white", activebackground="red", anchor=CENTER, command=exitProgram)
exit.place(x=470, y=500)

start = Button(root, text="Start listening..", font=("Garamond", 24), foreground="purple", activeforeground="white", bg="cyan", activebackground="cyan", command=mainLoop)
start.pack(padx=15, pady=7)
start.place(x=377, y=316,)

#root.wm_attributes('-transparentcolor','blue')
root.mainloop()
