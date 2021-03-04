#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#CRIAÇÃO DE UMA NOVA PALAVRA

palavra = input()
numero = input()
nova = ''

for i in range(len(palavra)):
    nova += palavra[i] + palavra[i] * int(numero[len(numero) - 1 - i])

print(nova)
