#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#QUANTIDADE DE USUÁRIOS

def quantidade_usuarios(cadastro):
    contador = 0
    for valor in cadastro.values():
            for e in valor:
                if e != 'administrador':
                    contador += 1

    return contador
   
