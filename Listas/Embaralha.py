def embaralha(p):
	import random
	aux = list(p)
	random.shuffle(aux)
	return ''.join(aux)

p = input('Digite uma palavra: ')
print(p)
p = embaralha(p)
print(p)