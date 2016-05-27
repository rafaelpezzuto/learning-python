import sys
arquivo_nome = sys.argv[1]
trecho = sys.argv[2]

linhas = open(arquivo_nome).readlines()
numero_linhas = len(linhas)
saida_texto = ''

for i in range (0, numero_linhas):
	if (trecho in linhas[i]):
		saida_texto = saida_texto + linhas[i]

print saida_texto