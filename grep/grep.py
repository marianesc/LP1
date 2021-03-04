#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#GREP

palavra = input()
n = int(input())

for k in range(n):
    frase = input()
    for i in range(len(frase) - 2):
        if palavra == frase[i] + frase[i + 1] + frase[i + 2]:
            print(frase)
