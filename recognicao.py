import pyaudio
import speech_recognition as sr

def arquivoParaTexto():
	print("Olá, seja bem vindo ao decodificador de audio para texto!\n\nO arquivo deve estar no formato FLAC!")
	path = input("Insira o caminho completo para o arquivo de áudio ")

	arch = sr.AudioFile(path)
	r = sr.Recognizer()
	with arch as source:
		print("ouvindo o arquivo!")
		audio = r.record(source)
		print("decodificando")


	try:
		
		frase = r.recognize_google(audio,language='pt-BR')
		file = open("file.txt", "w") 
		file.write(frase + "\n") 
		file.close()
		print("ok, criei um arquivo com nome de file.txt, olha lá!\n \nCodado por Guilherme Terriaga")
		
		
	except sr.UnknownValueError:
		print("poderia repetir por favor?")

	return frase
	
frase = arquivoParaTexto()