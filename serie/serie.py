#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#SÉRIE (8.8)

n = (100 - 8.8) / 0.2
contador = 8.8
print('{:.1f}'.format(contador))

for i in range(int(n)):
    contador += 0.2
    print('{:.1f}'.format(contador))
