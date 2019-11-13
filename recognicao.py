#primeiro programa em pyhton
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pyaudio
import speech_recognition as sr

def arquivoParaTexto():

	arch = sr.AudioFile('arq22.flac')
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
		print("ok, criei um arquivo .txt, olha lá!")
		
		
	except sr.UnknownValueError:
		print("can you repeat please?")

	return frase
	
frase = arquivoParaTexto()