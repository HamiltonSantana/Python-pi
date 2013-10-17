def ipvalido(ip):
	ip = ip.split('.')
	for byte in ip:
		if int(byte) > 255:
			return False
	return True
arq = open('IPS.txt')
validos = open('Validos.txt','w')
invalidos = open('Invalidos.txt','w')
for linha in arq.readlines():
	if ipvalido(linha):
		validos.write(linha)
	else:
		invalidos.write(linha)
arq.close()
validos.close()
invalidos.close()