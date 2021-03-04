#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#CHAVE SEGURA

chave = input()

i = 0
contador = 0

while i < len(chave):
    if i < len(chave) - 2 and chave[i] == chave[i + 1] and chave[i] == chave[i + 2]:
        print('Chave insegura. 3 caracteres consecutivos iguais.')
        break
    elif chave[i] == 'a' or chave[i] == 'e' or chave[i] == 'i' or chave[i] == 'o' or chave[i] == 'u':
        contador += 1
        if contador == 6:
            print('Chave insegura. 6 vogais.')
            break
    if i == len(chave) - 1:
        print('Chave segura!')
        break
    i += 1
