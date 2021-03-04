#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#CATEGORIAS

nome = input()
idade = int(input())

categoria = 0

if 5 <= idade <= 7:
    categoria = 'Infantil A'
    print('{}, {} anos, {}.'.format(nome, idade, categoria)) 
elif 8 <= idade <= 10:
    categoria = 'Infantil B'
    print('{}, {} anos, {}.'.format(nome, idade, categoria))
elif 11 <= idade <= 13:
    categoria = 'Juvenil A'
    print('{}, {} anos, {}.'.format(nome, idade, categoria))
elif 14 <= idade <= 17:
    categoria = 'Juvenil B'
    print('{}, {} anos, {}.'.format(nome, idade, categoria))
elif idade >= 17:
    categoria = 'Senior'
    print('{}, {} anos, {}.'.format(nome, idade, categoria))
else:
    categoria = 'Não pode competir'
    print('{}, {} anos, {}.'.format(nome, idade, categoria))

