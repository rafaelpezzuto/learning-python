import sys
arquivo_nome = sys.argv[1]

linhas = open(arquivo_nome).readlines()
nlinhas = len(linhas)
saida_texto = ''
max_tamanho_linha = 0

for i in range (0, nlinhas):
	if (len(linhas[i]) > max_tamanho_linha):
		max_tamanho_linha = len(linhas[i])

if (max_tamanho_linha % 2 == 0):
	max_tamanho_linha = max_tamanho_linha + 1

for k in range (0, nlinhas):
	linha_tamanho = len(linhas[k])
	espacos_adicionais = (max_tamanho_linha - linha_tamanho)/2
	saida_texto = saida_texto + espacos_adicionais * ' ' + linhas[k]

print saida_texto