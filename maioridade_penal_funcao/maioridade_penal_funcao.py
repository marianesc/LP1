#UFCG- PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#MAIORIDADE PENAL FUNÇÃO

def maioridade_penal(nomes, idades):
    lista_nomes = nomes.split()
    lista_idades = idades.split()
    maiores = ''
    for i in range(len(lista_idades)):
        if int(lista_idades[i]) >= 18 and maiores == '':
            maiores += lista_nomes[i]
        elif int(lista_idades[i]) >= 18:
            maiores += ' ' + lista_nomes[i]
    return maiores

