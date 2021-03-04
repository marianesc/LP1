#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#VALIDAÇÃO DE TRIÂNGULOS

a = int(input())
b = int(input())
c = int(input())

b_c = abs(b - c)
a_c = abs(a - c)
a_b = abs(a - b)

b_soma_c = b + c
a_soma_c = a + c
a_soma_b = a + b

perimetro = a + b + c

if b_soma_c < a < b_soma_c:
    print('triangulo valido. {}'.format(perimetro))
elif a_c < b < a_soma_c:
    print('triangulo valido. {}'.format(perimetro))
elif a_b < c < a_soma_b:
    print('triangulo valido. {}'.format(perimetro))
else:
    print('triangulo invalido.')
