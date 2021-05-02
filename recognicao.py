import pyaudio
import time
import speech_recognition as sr


def arquivoParaTexto():
    # print("Olá, seja bem vindo ao decodificador de audio para texto!\n\nO arquivo deve estar no formato FLAC!")
    # path = input("Insira o caminho completo para o arquivo de áudio ")

    # arch = sr.AudioFile(path)
    # r = sr.Recognizer()
    # with arch as source:
    #     print("ouvindo o arquivo!")
    #     audio = r.record(source)
    #     print("decodificando")
    microfone = sr.Recognizer()
    tempo = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with sr.Microphone() as source:
         microfone.adjust_for_ambient_noise(source)
         print("Diga alguma coisa: ")
         audio = microfone.listen(source)



    try:

        frase = microfone.recognize_google(audio, language='pt-BR')
        file = open(tempo+"arquivo o que foi dito.txt", "w")
        # print("Falado: "+frase)
        file.write(frase + "\n")
        file.close()
        print("ok, criei um arquivo com nome de o que foi dito.txt, olha lá!\n \nCodado por Guilherme Terriaga")

    except sr.UnknownValueError:
        print("poderia repetir por favor?")

    return frase


frase = arquivoParaTexto()
