import speech_recognition as sr
import pyttsx3
import pywhatkit as pw
import datetime
import wikipedia
import pyjokes



escucha = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',130)
"prueba"

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('Que quieres hacer...')
            voces = escucha.listen(source)
            command = escucha.recognize_google(voces, language = 'es-ES')
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'reproduce' in command:
        song = command.replace('reproduce', '')
        talk('Reproduciendo ' + song)
        pw.playonyt(song)
    elif 'dime la hora' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Son las ' + time)
    elif 'quien mierda es' in command:
        person = command.replace('quien mierda es', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'cuenta un chiste' in command:
        talk(pyjokes.get_joke())
    elif 'enviar mensaje' in command:
        talk("Enviando mensaje")
        pw.sendwhatmsg("+543513992956", "Te amo muchisimo", 22,26,15)
    elif 'familia cool' in command:
        pw.sendwhatmsg_to_group("KLcCR2qMEpsID06bfBrcBf","holiss flia como estan?",23,45,15)
        talk("Enviando mensaje")
    else:
        talk('Por favor repite que no entendi...')


while True:
    run_jarvis()