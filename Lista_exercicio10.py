cigar = float(input("Quantos cigarros fuma por dia: "))
temp = float(input("Quantos ha quantos anos fuma: "))

tempo = temp * 365
cigarro = tempo * (cigar * 10)
cigarro = cigarro / 1440 

print("Voce tem %.f dias a menos." %cigarro)
