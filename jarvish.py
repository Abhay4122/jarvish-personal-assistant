import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
# import googlesearch
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    '''Wish me Function is used for Return Hours Value From 0 to 23'''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Sir')
    elif hour >= 12 and hour < 16:
        speak('Good After Noon Sir')
    else:
        speak('Good Evening Sir')
    speak('I am Jarvish, Please tell me how may i help you?')

def tek_cmd():
    '''tek_cmd Or Take Command Function is Used for Take Command in Voice From Commander With the Help of Microphone'''
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(sourse)
    
    try:
        print('Recognizinging...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)
        print('Say that again Please...')
        return 'None'
    return query

def sendEmail(t_o, cont_ent):
    # search SMTPlib on google for focumentation
    # and also enable less secure apps
    pass_word = 'Your Password'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your_email', pass_word)
    server.sendmail('Your_email', t_o, cont_ent)
    server.close()

if __name__ == "__main__":
    wish_me()
    # tek_cmd()
    while True:
        tek_cmd_query = tek_cmd().lower()

        # Logic for execute task based on query
        if 'wikipedia' in tek_cmd_query:
            speak('Searching wikipedia...')
            tek_cmd_query = tek_cmd_query.replace('wikipedia', '')
            result = wikipedia.summary(tek_cmd_query, sentences=2)
            speak('According To wikipedia')
            print(result)
            speak(result)

        elif 'thank you jarvish' in tek_cmd_query:
            speak('Your Welcome Sir.')

        elif 'open youtube' in tek_cmd_query:
            webbrowser.open('https://www.youtube.com/')

        elif 'open localhost' in tek_cmd_query:
            webbrowser.open('http://127.0.0.1:8000/')

        elif 'play music' in tek_cmd_query or 'play song' in tek_cmd_query or 'open music' in tek_cmd_query or 'open song' in tek_cmd_query:
            music_dir = 'E:\\Music\\Himesh resamiya'
            songs = os.listdir(music_dir)       # Show the List of the Musics
            # print(songs)
            speak(f'Ok Playing Music')
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs))]))

        elif 'the time' in tek_cmd_query:
            ti_me = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {ti_me}')
        
        elif 'open code' in tek_cmd_query:
            code_path = 'C:\\Users\\Abhay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            speak('Ok Opening Visual Studio Code')
            os.startfile(code_path)

        elif 'email to abhay' in tek_cmd_query:
            try:
                speak('What should i say')
                content = tek_cmd()
                to = 'avaneesh54321@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent Successfully')
            except Exception as e:
                print(e)
                speak('Sorry Email Not send')

        elif 'exit jarvish' in tek_cmd_query:
            speak('Thank you, If you need help then Anytime call me')
            break
        else:
            speak('Sorry the command not found Please try again')