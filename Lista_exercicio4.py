a = float(input("Digite o salario: "))
b = int(input("Digite o reajuste: "))

b = b /100
c = b * a
a = a + c

print("O reajuste foi de: ",c," e o salario apos reajuste é: ",a)
