#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#MAIS VELHOS PRIMEIRO

def idosos_inicio(lista):
    auxiliar = 0
    for i in range(len(lista)):
        if lista[i] >= 60:
            lista[i], lista[auxiliar] = lista[auxiliar], lista[i]
            auxiliar += 1

