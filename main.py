import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime as dt
import wikipedia as wiki
import webbrowser as web

listener = sr.Recognizer()
engine = pyttsx3.init()

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',0.5)    # setting up volume level  between 0 and 1

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print('listening...')
            global command
            voice = listener.listen(source)
            command= listener.recognize_google(voice)
            command=command.lower()
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass
    return command

talk('How can I help you ? ')
 
def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', ' ')
        talk('playing' + song)
        kit.playonyt(song)
        talk('How else can I help ?')
        run_alexa()
    elif 'bad' in command:
        talk('I hope your day gets better. How else can I help ?')
        run_alexa()
    elif 'good' in command:
        talk('I\'m glad to hear that. How else can I help ?')
        run_alexa()
    elif 'time' in command:
        time = dt.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time + '.  How else can I help ?')
        run_alexa()
    elif 'search for' in command:
        search = command.replace('search for', '')
        kit.search(search)
        info = wiki.summary(search, 1)
        talk(info + '.  How else can I help ?')
        run_alexa()
    elif 'open Elizabeth\'s site' in command:
        web.open('https://elizabethsmrdelmassage.com', new = 2)
        talk('How else can I help ?')
        run_alexa()
    elif 'done talking' in command:
        talk('Talk to you later.')
    else:
        talk('I don\'t understand.')
        run_alexa()

run_alexa()
