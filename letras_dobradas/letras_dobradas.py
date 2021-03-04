#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#PALAVRAS COM LETRAS DOBRADAS

n = int(input())
contador = 0
contador2 = 0
dobradas = []
nao_dobradas = []
dobrada = False

for k in range(n):
    palavra = input()
    for i in range(len(palavra) - 1) :
        if palavra[i] == palavra[i + 1]:
            dobrada = True
            break
        else:
            dobrada = False
    if dobrada:
        dobradas.append(palavra)
    else:
        nao_dobradas.append(palavra)

print('{} palavra(s) com letras dobradas:'.format(len(dobradas)))

for i in range(len(dobradas)):
    print(dobradas[i])

print('---')
print('{} palavra(s) sem letras dobradas:'.format(len(nao_dobradas)))

for i in range(len(nao_dobradas)):
        print(nao_dobradas[i])
