data = input('Data: ')
meses = ['janeiro','fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
data = data.split('/')
mes = data[1]
mes = int(mes) - 1
data[1] = meses[mes]
print('/'.join(data))