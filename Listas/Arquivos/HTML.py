arq = open('teste.html','w',encoding='utf-8')
arq.write('''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Minha Pagina Salva em python</title>
</head>
<body>
MINHA Pagina
</body>
</html>	
''')
arq.close()