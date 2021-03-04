n = int(input())
cont0 = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0 
cont6 = 0
cont7 = 0
cont8 = 0
cont9 = 0

for i in range(n):
    matricula = input()
    for e in matricula:
        if e == '0':
            cont0 += 1
        elif e == '1':
            cont1 += 1
        elif e == '2':
            cont2 += 1
        elif e == '3':
            cont3 += 1
        elif e == '4':
            cont4 += 1
        elif e == '5':
            cont5 += 1
        elif e == '6':
            cont6 += 1
        elif e == '7':
            cont7 += 1
        elif e == '8':
            cont8 += 1
        elif e == '9':
            cont9 += 1
        
if cont0 >= cont1 and cont0 >= cont2 and cont0 >= cont3 and cont0 >= cont4 and cont0 >= cont5 and cont0 >= cont6 and cont0 >= cont7 and cont0 >= cont8 and cont0 >= cont9:
    print('0', str(cont0))
elif cont1 >= cont0 and cont1 >= cont2 and cont1 >= cont3 and cont1 >= cont4 and cont1 >= cont5 and cont1 >= cont6 and cont1 >= cont7 and cont1 >= cont8 and cont1 >= cont9:
    print('1', str(cont1))
elif cont2 >= cont0 and cont2 >= cont1 and cont2 >= cont3 and cont2 >= cont4 and cont2 >= cont5 and cont2 >= cont6 and cont2 >= cont7 and cont2 >= cont8 and cont2 >= cont9:
    print('2', str(cont2))
elif cont3 >= cont0 and cont3 >= cont1 and cont3 >= cont2 and cont3 >= cont4 and cont3 >= cont5 and cont3 >= cont6 and cont3 >= cont7 and cont3 >= cont8 and cont3 >= cont9:
    print('3', str(cont3))
elif cont4 >= cont0 and cont4 >= cont1 and cont4 >= cont2 and cont4 >= cont3 and cont4 >= cont5 and cont4 >= cont6 and cont4 >= cont7 and cont4 >= cont8 and cont4 >= cont9:
    print('4', str(cont4))
elif cont5 >= cont0 and cont5 >= cont1 and cont5 >= cont2 and cont5 >= cont3 and cont5 >= cont4 and cont5 >= cont6 and cont5 >= cont7 and cont5 >= cont8 and cont5 >= cont9:
    print('5', str(cont5))
elif cont6 >= cont0 and cont6 >= cont1 and cont6 >= cont2 and cont6 >= cont3 and cont6 >= cont4 and cont6 >= cont5 and cont6 >= cont7 and cont6 >= cont8 and cont6 >= cont9:
    print('6', str(cont6))
elif cont7 >= cont0 and cont7 >= cont1 and cont7 >= cont2 and cont7 >= cont3 and cont7 >= cont4 and cont7 >= cont5 and cont7 >= cont6 and cont7 >= cont8 and cont7 >= cont9:
    print('7', str(cont7))
elif cont8 >= cont0 and cont8 >= cont1 and cont8 >= cont2 and cont8 >= cont3 and cont8 >= cont4 and cont8 >= cont5 and cont8 >= cont6 and cont8 >= cont7 and cont8 >= cont9:
    print('8', str(cont8))
elif cont9 >= cont0 and cont9 >= cont1 and cont9 >= cont2 and cont9 >= cont3 and cont9 >= cont4 and cont9 >= cont5 and cont9 >= cont6 and cont9 >= cont7 and cont9 >= cont8:
    print('9', str(cont9))
