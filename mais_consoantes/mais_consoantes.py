#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#MAIS CONSOANTES

contador = 0
vogais = ['A','a','E','e','I','i','O','o','U','u']

while True:
    palavra = input()
    contador += 1
    vogal = 0
    consoante = 0
    for el in palavra:
        EhVogal = False
        for e in vogais:
            if el == e:
                EhVogal = True
                break
        if EhVogal:
            vogal += 1
        else:
            consoante += 1
    if consoante > vogal:
        break

print(contador)
