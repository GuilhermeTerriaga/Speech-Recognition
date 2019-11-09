import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pyaudio
import speech_recognition as sr

def arquivoParaTexto():

	arch = sr.AudioFile('arq.wav')
	r = sr.Recognizer()
	with arch as source:
		print("ouvindo o arquivo!")
		
		audio = r.record(source)
		print("decodificando")


	try:
		
		frase = r.recognize_google(audio,language='pt-BR')
		
		file = open("file.txt", "w") 
		file.write(frase) 
		file.close()

		
	except sr.UnknownValueError:
		print("Por favor, repete?")

	return frase
	
frase = arquivoParaTexto()