notas = []
i = 1
media = 0
while i<= 4:
	n = int(input("Digite sua nota: "))
	notas.append(n)
	media = n + media
	i += 1

print ("As notas sao ", notas)
print ("A media das notas é: ", media/4)