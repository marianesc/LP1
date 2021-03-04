#UFCG
#PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#QUADRADO NA CIRCUNFERÊNCIA

import math

r = float(input())

diametro = 2 * r
l = (diametro ** 2 / 2) ** 0.5
area_quadrado = l * l
area_circunferencia = math.pi * r ** 2

espaco = area_circunferencia - area_quadrado

print('Área não comum: {:.5f}'.format(espaco))
