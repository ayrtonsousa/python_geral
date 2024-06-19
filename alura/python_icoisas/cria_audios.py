from gtts import gTTS
from playsound import playsound

def cria_audio(audio):
    tts = gTTS(audio, lang="pt-br")
    tts.save('audios/ola.mp3')
    playsound('audios/ola.mp3')


cria_audio('Oi eu sou o Ayrton')