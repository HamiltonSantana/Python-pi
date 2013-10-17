import random
a =int(input("Digite seu chute: "))
g = random.randint(1,101)
tent = 2
while  tent >= 1:
	if a > g:
		print ('Chute mais baixo')
		a = int(input("Digite denovo: "))
	elif a < g:
		print('Chute mais alto')
		a = int(input('Digite denovo: '))
	elif a == g:
		break
	tent -= 1
if tent >= 0 and a == g:
	print('Voce ganhou')
else:
	print('You loose !')
print('Fim')