#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#SELECIONA DIVISORES EM UMA LISTA

def filtra_divisores(lista):
    for k in range(len(lista) - 1, -1, -1):
        num_str = str(lista[k])
        contador = 0
        for i in range(len(num_str)):
            contador += int(num_str[i])
        if lista[k]  % contador != 0:
            lista.pop(k)

