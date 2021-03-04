#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#ESTOQUE DE LIVROS

def ausentes(estoque):
    contador = 0
    for e in estoque.values():
        if e == 0:
            contador += 1

    return contador

