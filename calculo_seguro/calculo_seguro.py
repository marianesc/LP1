#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#CÁLCULO DE SEGURO

def calcula_seguro(valor,lista):
    pontuacao = 0
    nova_lista = []
    for i in range(len(lista)):
        if i == 0:
            if lista[0] <= 21: pontuacao += 20
            elif 22 <= lista[0] >= 30: pontuacao += 15
            elif 31 <= lista[0] >= 40: pontuacao += 12
            elif 41 <= lista[0] >= 60: pontuacao += 10
            elif lista[0] > 60: pontuacao += 20

        elif i == 1:
            if lista[1] == True: pontuacao += 10
            else: pontuacao += 20

        elif i == 2:
            if lista[2] == True: pontuacao += 20
            else: pontuacao += 10

        elif i == 3:
            if lista[3] == True: pontuacao += 20
            else: pontuacao += 10

        elif i == 4:
            if lista[4] == True: pontuacao += 20
            else: pontuacao += 10

        elif i == 5:
            if lista[5] == True: pontuacao += 10
            else: pontuacao += 20

        elif i == 6:
            if lista[6] == 'Lazer': pontuacao += 20
            elif lista[6] == 'Trabalho': pontuacao += 10
            elif lista[6] == 'Misto': pontuacao += 20

    nova_lista.append(pontuacao)

    if pontuacao <= 80:
        nova_lista.append("Risco Baixo")
        seguro = 0.1 * valor
        nova_lista.append(seguro)
    elif 80 < pontuacao <= 100:
        nova_lista.append("Risco Medio")
        seguro = 0.2 * valor
        nova_lista.append(seguro)
    else:
        nova_lista.append("Risco Alto")
        seguro = 0.3 * valor
        nova_lista.append(seguro)

    return nova_lista

