i = 8
nome = str(input("Digite uma palavra: "))
while i > 0:
	if i == 8:
		nome1 = nome[i-1:i]
	else:
		nome1 = nome1+nome[i-1:i]
	i -= 1
if nome1 == nome:
	print('A palavra: %s é uma palindra' %nome)
else:
	print('Uma palavra comum',nome)