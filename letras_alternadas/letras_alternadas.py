#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#LETRAS ALTERNADAS

palavra = input()
lista = []

#print(palavra[0::2])

for i in range(0, len(palavra), 2):
    lista.append(palavra[i])

print(''.join(lista))
