a = str(input("Escolha uma opcao: M - metros, MM - milimetros")) 

if a == "M":
	x = int(input("Digite a metragem: "))
	b  = x * 1000
if a == "MM":
	x = float(input("Digite a milimetragem: "))
	c  = x / 1000
if a == "M":
	print ("A convercao fica de",x," metros para",b," milimetros")
else :
	print ("A convercao fica de",x," milimetros para",c,"  metros")
