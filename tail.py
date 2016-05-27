import sys
arquivo_nome = sys.argv[1]

linhas = open(arquivo_nome).readlines()
numero_linhas = len(linhas)
saida_texto = ''

if not (numero_linhas <= 10):
	for i in range (numero_linhas - 10, numero_linhas):
		saida_texto = saida_texto + linhas[i]

	print saida_texto
else :
	print linhas