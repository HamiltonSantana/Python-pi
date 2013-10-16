import random

lista = []
numero = random.randint(10,100)
while not len(lista) == 15:
	while numero in lista:
	 	numero = random.randint(10,100)
	lista.append(numero)  
lista.sort()
print(lista)