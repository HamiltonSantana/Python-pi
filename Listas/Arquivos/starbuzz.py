import urllib.request
import time
preco = 42.00
while preco >= 4.74:
	pagina = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
	texto = pagina.read().decode('utf8')
	onde = texto.find(">$")
	inicio = onde +2
	fim = inicio + 4
	preco = float(texto[inicio:fim])
	if preco >= 4.74:
		time.sleep(600)
print('Compre Preco:%.2f' %preco)