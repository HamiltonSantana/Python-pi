n = int(input("Digite o ano: "))

if not str(n)[2:4] == '00':
	if n % 4 == 0:
		print('Ano bissesto')
	else:
		print('Ano nao bissesto')
if str(n)[2:4] == '00':
	if n % 400 == 0:
		print('Ano bissesto')
	else:
		print('Ano nao bissesto')