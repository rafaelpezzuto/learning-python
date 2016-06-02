# problem 7
def max (lista):
	if (len (lista) > 0):
		maxa = lista[0]
		for i in range (0, len (lista)):
			if (lista[i] > maxa):
				maxa = lista[i]
		return maxa

# problem 7
def min (lista):
	if (len (lista) > 0):
		mina = lista[0]
		for i in range (0, len (lista)):
			if (lista[i] < mina):
				mina = lista[i]
		return mina

# problem 8
def cumulative_sum (lista):
	if (len (lista) > 0):
		sum = lista[0]
		cumsum = [sum]
		for i in range (1, len (lista)):
			sum = sum + lista[i]
			cumsum.append (sum)
		return cumsum

# problem 9
def cumulative_product (lista):
	if (len (lista) > 0):
		sum = lista[0]
		cumsum = [sum]
		for i in range (1, len (lista)):
			sum = sum * lista[i]
			cumsum.append (sum)
		return cumsum

# problem 10
# def unique (lista):
# 	if (len (lista) > 0):
# 		uniquelist = [lista[0]]
# 		for i in range (1, len (lista)):
# 			if not (lista[i] in uniquelist):
# 				uniquelist.append (lista[i])
# 		return uniquelist

# problem 14
# def unique (lista, key):
# 	if (len (lista) > 0):
# 		uniquelist = [key (lista[0])]
# 		for i in range (1, len (lista)):
# 			if not (key (lista[i]) in uniquelist):
# 				uniquelist.append (key (lista[i]))
# 		return uniquelist

# problem 15
def unique (lista, key):
	if (len (lista) > 0):
		uniquelist = {key (lista[0])}
		for i in range (1, len (lista)):
			uniquelist.add (key (lista[i]))
		return uniquelist

# problem 11
def dups (lista):
	if (len (lista) > 0):
		uniquelist = [lista[0]]
		dupslist = []
		for i in range (1, len (lista)):
			if not (lista[i] in uniquelist):
				uniquelist.append (lista[i])
			else:
				dupslist.append (lista[i])
		return dupslist

# problem 12
def group (lista, k):
	if (len (lista) > 0 and k > 0):
		groupslist = []
		for i in range (0, len (lista), k):
			groupslist.append (lista[i:i + k])
		return groupslist

# problem 13
def lensort (lista):
		return sorted (lista, key = lambda x : len (x))

# problem 16
def extsort (lista):
	return sorted (lista, key = lambda x : x.split ('.')[1])

# problem 24
def zip (lista1, lista2):
	return [(x,y) for indx, x in enumerate (lista1) for indy, y in enumerate (lista2) if indx == indy]

# problem 25
def map (funcao, lista):
	return [funcao(x) for x in lista]

# problem 26
def filter (filtro, lista):
	return [x for x in lista if filtro (x)]

# problem 27
def triplets (n):
	return [(x, y, z) for x in range (1, n) for y in range (x, n) for z in range (y, n) if x + y == z]

# problem 28: preciso implementar sem usar a funcao enumerate do python
def myenumerate (lista):
	return [(indice, valor) for indice, valor in enumerate (lista)]

# problem 29
def array (linhas, colunas):
	return [[None for x in range (linhas)] for y in range (colunas)]

# problem 30
def parse_csv (arquivo):
	dados = open (arquivo).readlines()
	return [x.strip ('\n'). split(',') for x in dados]
