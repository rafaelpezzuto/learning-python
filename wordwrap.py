import sys
arquivo_nome = sys.argv[1]
max_width = int(sys.argv[2])

linhas = open(arquivo_nome).readlines()
nlinhas = len(linhas)
saida_texto = ''

for i in range (0, nlinhas):
	palavras_linha = linhas[i].split()
	npalavras = len(palavras_linha)
	acumulado = ''

	for k in range (0, npalavras):
		palavra_atual = palavras_linha[k]

		if (len(acumulado + palavra_atual) < max_width):
			saida_texto = saida_texto + palavra_atual + ' '
			acumulado = acumulado + palavra_atual + ' '
		else :
			acumulado = palavra_atual + ' '
			saida_texto = saida_texto + '\n' + acumulado

	saida_texto = saida_texto + '\n'

print saida_texto.strip()