rodados = int(input("Digite o numero de kilometros rodados: "))
dias = int(input("Digite por quantos dias esteve com o carro: "))

apagar = (rodados * 0.15)+(dias * 60)

print("O valor que devera ser pago pelo alugel é: R$%.2f " %apagar)
