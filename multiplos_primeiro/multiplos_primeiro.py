#UFGC - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#SOMA OS MÚLTIPLOS DO PRIMEIRO ELEMENTO DE UMA LISTA

referencia = int(input())
contador = 0

for k in range(10):
    numero = int(input())
    if numero % referencia == 0:
        contador += numero

print(contador)
