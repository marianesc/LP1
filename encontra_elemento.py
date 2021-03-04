n = input()
numeros = input()
numeros.split()
boo = False

for i in range(len(numeros)):
    if numeros[i] == n:
        print('sim')
        boo = True
        break
    
if boo == False:
    print('não')
