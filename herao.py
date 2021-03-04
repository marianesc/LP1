#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#UTILIZANDO O TEOREMA DE HERÃO PARA CALCULAR A ÁREA DE TRIÂNGULOS

n = int(input())
lista_maiores = []
lista = []
contador = 0
soma = 0

for k in range(n):
    triangulo = input().split()
    s = (float(triangulo[0]) + float(triangulo[1]) + float(triangulo[2])) / 2
    area = (s * (s - float(triangulo[0])) * (s - float(triangulo[1])) * (s - float(triangulo[2]))) ** 0.5
    lista.append(str(area))
    if area > 100:
        contador += 1
        soma += area
        lista_maiores.append(str(area))

for i in range(len(lista)):
    print('Área {}: {:.2f}'.format(i + 1, float(lista[i])))

if contador > 0:
    media = soma / len(lista_maiores)
    print('Número maiores: {}, área média: {:.2f}'.format(contador, media))

