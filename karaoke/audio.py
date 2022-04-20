import speech_recognition as sr

def ouvir_microfone():

    microfone = sr.Recognizer()
    with sr.Microphone() as source:
#        microfone.adjust_for_ambient_noise(source)

        print ('fale :')

        audio = microfone.listen(source)

    try:

        frase = microfone.recognize_google(audio,language='pt-BR')

        print (frase)

    except sr.UnknownValueError:
        print ('erro')

    return frase

ouvir_microfone()

