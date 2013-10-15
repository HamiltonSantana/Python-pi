a = int(input("Digite os dias: "))
b = int(input("Digite as horas: "))
c = int(input("Digite os minutos: "))
d = int(input("Digite os segundos: "))

a = a * 86400
b = b * 3600
c = c * 60

z = a+b+c+d

print ("O total de dias, horas, minutos e segundos em segundos é: ",z,"segs")
