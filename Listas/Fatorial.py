def fatorial(n):
	if n == 1:
		return 1
	else:
		return(n * fatorial(n-1))

n = int(input('Fatorial: '))

print("O fatoria de %d é: %d" %(n,fatorial(n)))