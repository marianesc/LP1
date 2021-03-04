#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#QUANTAS PAS?

razao = int(input())
contador = 0

while True:
    numeros = input()
    sequencia = numeros.split()
    if numeros == 'fim':
        break
    for i in range(1, len(sequencia)):
        if int(sequencia[i]) - int(sequencia[i - 1]) == razao:
            Epa = True
        else:
            Epa = False

    if Epa:
        contador += 1

print(contador)
