import sys
import os

diretorio = sys.argv[1]

if (os.path.isdir (diretorio)):
	arquivos = os.listdir (diretorio)
	contador = {}
	arquivos_sem_extensao = []
	for i in range (len (arquivos)):
		try:
			extensao = arquivos[i].split ('.')[1]
			contador[extensao] = contador.get (extensao, 0) + 1
		except IndexError, e:
			arquivos_sem_extensao.append (arquivos[i])

	contador_ordenado = sorted (contador, key = lambda x : contador[x], reverse = True)

	for extensao in contador_ordenado:
		print extensao, contador[extensao]
else:
	print 'O caminho especificado nao eh um diretorio'