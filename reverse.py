import sys
arquivo_nome = sys.argv[1]

linhas = open(arquivo_nome).readlines()
numero_linhas = len(linhas)
saida_texto = ''

for i in range (0, numero_linhas):
	saida_texto = saida_texto + linhas[numero_linhas - i - 1]

print saida_texto