#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#CONTA CARACTERES INVERSA

palavra = input()
contador = 0

for i in range(len(palavra)):
    if palavra[i] == palavra[len(palavra) - 1 - i]:
        contador += 1

print('A palavra {} contém {} caractere(s) coincidente(s) com a sua inversa.'.format(palavra, contador))
