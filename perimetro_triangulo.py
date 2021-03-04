#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#PERÍMETRO DE TRIÂNGULO

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

d1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
d2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
d3 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

perimetro = d1 + d2 + d3 

print('O perímetro é de {:.2f}'.format(perimetro))
