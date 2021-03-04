#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#IMPRIME RANKING

n_times = int(input())
l_ponto = []
l_nome = []
l_posicao = []
ultimo_ponto = 0 
ultima_posicao = 1

for i in range(n_times):
    nome = input()
    ponto = int(input())

    if ponto == ultimo_ponto:
        posicao = ultima_posicao

    else:
        posicao = i + 1
        ultima_posicao = posicao

    ultimo_ponto = ponto
    l_ponto.append(ponto)
    l_nome.append(nome)
    l_posicao.append(posicao)

for i in range(n_times):
    print('{}. {} ({})'.format(l_posicao[i], l_nome[i], l_ponto[i]))
