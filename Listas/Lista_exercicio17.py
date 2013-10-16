palavra = input("Palavra: ")

n = len(palavra)
i = 1
print (palavra)
while i <= n:
	if palavra[i-1 :i] in 'aeiou':
		print(palavra[i-1:i])
		palavra = '*' + palavra[::i::]
		print(palavra)
	i += 1
print (palavra)
