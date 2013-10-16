def aleatorios():
	import random
	lista = list(range(15))
	for i in range(15):
		lista[i] = random.randint(10,100)
	return lista
print(aleatorios())