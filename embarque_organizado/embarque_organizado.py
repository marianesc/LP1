#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#EMBARQUE ORGANIZADO

ordem = input().split()

misturado = False
pares = 0 
i = 0

while i < len(ordem) and not misturado:
    num = int(ordem[i])

    if num % 2 == 0:
        pares += 1
    elif pares > 0:
        misturado = True

    i += 1

if misturado:  print('erro')
else: print('ok')
