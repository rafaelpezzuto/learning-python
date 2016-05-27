import sys
arquivo_nome = sys.argv[1]
max_width = int(sys.argv[2])

linhas = open(arquivo_nome).readlines()
numero_linhas = len(linhas)
saida_texto = ''

for i in range (0, numero_linhas):
	linha_width = len(linhas[i])
	fracoes = linha_width / max_width
	if (linha_width >= max_width):
		for z in range (0, fracoes + 1):
			saida_texto = saida_texto + linhas[i][z*max_width:(z+1)*max_width]
			if not (z == fracoes):
				 saida_texto = saida_texto + '\n'
	else :
		saida_texto = saida_texto + linhas[i]

print saida_texto.strip()