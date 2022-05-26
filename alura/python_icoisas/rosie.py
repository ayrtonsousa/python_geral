import speech_recognition as sr

#biblioteca sera descontinuada
# obtain audio from the microphone
def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando o audio")
        audio = microfone.listen(source)


    # recognize speech using Google Speech Recognition
    try:
        print(microfone.recognize_google(audio,language='pt-BR'))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

monitora_audio()