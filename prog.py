def getMaximo(lista):
	max_num = lista[0]
	for i in lista:
		if i > max_num:
			max_num = i
	return max_num

def getMinimo(lista):
	min_num = lista[0]
	for i in lista:
		if i > min_num:
			min_num = i
	return min_num
