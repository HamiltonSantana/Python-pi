arquivo = open('mensagem.txt','r')

mgs = arquivo.readline()
troca =''
i = 0
while i < len(mgs):
	if mgs[i] in 'aeiou':
		troca = troca + '*'
	else:
		troca = troca + mgs[i]
	i += 1
cripto = open('cripto.txt','w')
cripto.write(troca)
cripto.close()
arquivo.close()