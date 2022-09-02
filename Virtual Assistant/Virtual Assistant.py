import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


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



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
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
            speak('i as created by Kunal Awari')


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



#music
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            speak("playing ")
            os.startfile(os.path.join(music_dir, songs[15]))
#datetime
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:%A:%d:%B:%Y")
            speak(f"Sir, the time is {strTime}")



#joke
        elif 'joke' in query:
            #print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

#game
        elif'play game' in query:
            webbrowser.open('https://elgoog.im/t-rex/')

#in youtube

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)