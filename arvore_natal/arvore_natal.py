#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#DESENHANDO UMA ÁRVORE DE NATAL

altura = int(input())
contador = 0
for i in range(altura):
    print((' ' * (altura - i - 1)) + ('o' * (1 + contador)))
    contador += 2

print((' ' * (altura - 1)) + ('o' * 1))
