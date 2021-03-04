#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#CRIPTOGRAFANDO UMA SENHA

palavra = input()
vogais = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O']
palavra_modificada = ''
contador = 0

for letra in palavra[1:]:
    if letra == vogais[0] or letra == vogais[1]:
        letra = '4'
        contador += 1
    elif letra == vogais[2] or letra == vogais[3]:
        letra = '3'
        contador += 1
    elif letra == vogais[4] or letra == vogais[5]:
        letra = '1'
        contador += 1
    elif letra == vogais[6] or letra == vogais[7]:
        letra = '0'
        contador += 1
    palavra_modificada += letra
print('{}{} ({} troca(s))'.format(palavra[0], palavra_modificada, contador))

