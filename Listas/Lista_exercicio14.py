letras = []
i = 1
cont = 0
while i<= 10 :
	n = str(input("Digite uma letra: "))
	letras.append(n)
	if n not in 'aeiou':
		cont += 1
	i += 1
print("Vetor lido: ",letras)
print("Consoantes lidas", cont)