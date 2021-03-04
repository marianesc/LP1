#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#GET ITENS

def get_items(valores,indices):
    lista = []
    for e in indices:
        for i in range(len(valores)):
            if i == e:
                lista.append(valores[i])
                break
            elif e > len(valores) - 1:
                lista.append(None)
                break

    return lista

