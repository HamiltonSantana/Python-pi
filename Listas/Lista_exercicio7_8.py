opcao = int(input("Digite a convercao 1 - C para F, 2 - F para C:\n"))

if opcao == 1:
	temp = int(input("Digite a temperatura em Celsius:"))
	fahren = (9 * temp / 5) + 32
	print("A convercao de celsius para fahrenheit fica: %.1fºF" %fahren)

else:
	temp = int(input("Digite a temperatura em Fahrenheit: "))
	cels = ((temp-32) * 5) / 9
	print("A convercao de fahrenheit para celsius fica: %1.fºC" %cels)
