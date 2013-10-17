import random
secreto = random.randint(1,100)
chute = int(input('CHUTA AI MANO: '))
cont = 0
while True:
	if chute == secreto and cont == 0:
		print('FDP vc ta usando hack kk. numero chutado %d' %secreto)
		break
	if chute == secreto and cont == 1:
		print('Sortudo safado kk. numero chutado %d' %secreto)
		break
	if chute == secreto and cont == 2:
		print ('kkkkkkkkkkkk')
		break
	if chute == secreto and cont >= 3:
		print('Um noob msm kkk ')
		break
	print("Chuta mais alto animal --' " if chute < secreto else "Chuuta mais abaixo anta >.<")
	chute = int(input())
	cont += 1
print ('Fim do jogo. Sua bixa kk')