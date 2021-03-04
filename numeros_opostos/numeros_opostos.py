#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#LISTA COM NÚMEROS OPOSTOS

def lista_so_com_oposto(lista):
    for i in range(len(lista) - 1, -1, -1):
        n_oposto = True 
        for j in lista:
            if lista[i] + j == 0:
                n_oposto = False
                break
        if n_oposto:
            lista.pop(i)

