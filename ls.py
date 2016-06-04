import sys
import os

diretorio = sys.argv[1]

if (os.path.isdir (diretorio)):
	arquivos = sorted(os.listdir (diretorio))
	for i in range (len (arquivos)):
		print arquivos[i]
else:
	print 'O caminho especificado nao eh um diretorio'