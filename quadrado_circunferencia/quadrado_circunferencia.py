#UFCG
#PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#QUADRADO INSCRITO NA CIRCUNFERÊNCIA

import math

lq = float(input())

diametro = (2 * lq **2) ** 0.5
r = diametro / 2

perimetro = 2 * math.pi * r
area = math.pi * r ** 2

print('Perímetro: {:.5f}'.format(perimetro))
print('Área: {:.5f}'.format(area))
