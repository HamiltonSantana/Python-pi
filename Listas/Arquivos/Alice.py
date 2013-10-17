arq = open('AliceInWonderland.txt')
texto = arq.read()
texto = texto.lower()
import string
for i in string.punctuation:
	texto = texto.replace(i,'')
texto = texto.split()

dic = {}
for p in texto:
	if p not in dic:
		dic[p] = 1
	else:
		dic[p] += 1
print ('Alice apareceu %s vezes' %dic['alice'])
arq.close()