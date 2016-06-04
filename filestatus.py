import os
import sys
import time

diretorio = sys.argv[1]

if (os.path.isdir (diretorio)):
	diretorio_comando = os.getcwd()
	os.chdir (diretorio)
	arquivos = sorted(os.listdir (diretorio))
	print 'Name\t\tSize\tModification Date'
	for i in range (len (arquivos)):
		arquivos[i].replace(" ", "\ ")
		length = str(os.stat(arquivos[i])[6])
		modification_date = time.asctime (time.localtime (os.stat (arquivos[i])[8]))

		if (len (arquivos[i]) >= 8):
			print arquivos[i] + '\t' + length + '\t' + modification_date
		else:
			print arquivos[i] + '\t\t' + length + '\t' + modification_date
	os.chdir (diretorio_comando)
else:
	print 'O caminho especificado nao eh um diretorio'