#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#POSIÇÕES DE UM ELEMENTO EM UMA SEQUÊNCIA

num = input()
seq = input().split()
lista = []
saida = ''
for i in range(len(seq)):
    if num == seq[i]:
        lista.append(str(i))

if len(lista) > 0:
    for i in range(len(lista)):
        if i == len(lista) - 1:
            saida += lista[i]
        else:
            saida += lista[i] + ' '
    print(saida)

else:
    print('-1')
