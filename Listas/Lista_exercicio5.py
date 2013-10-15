merc = float(input("Digite o valor da mercadoria: "))
desc = int(input("Digite o valor do desconto: "))

desc = desc
newdesc = (desc/100) * merc
newmerc = merc - newdesc

print("O desconto foi de:%d e o valor do desconto foi de: %.3f. O valor mais o desconto é de: %.3f" %(desc, newdesc, newmerc))
