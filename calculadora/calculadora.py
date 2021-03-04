#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#CALCULADORA

i = 0
while i == 0:

    dados = input()
    operacao = dados.split()
    
    if operacao[i] == '1':
        def adicao(operacao):
            for i in range(1, len(operacao)):
                soma = int(operacao[1]) + int(operacao[2])
                return soma
                break
        print(adicao(operacao))

    elif operacao[i] == '2':
        def subtracao(operacao):
            for i in range(1, len(operacao)):
                subtracao = int(operacao[1]) - int(operacao[2])
                return subtracao
                break
        print(subtracao(operacao))

    elif operacao[i] == '3':
        def multiplicacao(operacao):
            for i in range(1, len(operacao)):
                multiplicacao = int(operacao[1]) * int(operacao[2])
                return multiplicacao
                break
        print(multiplicacao(operacao))

    elif operacao[i] == '4':
        def divisao(operacao):
            for i in range(1, len(operacao)):
                if operacao[2] == '0':
                    return 'Erro: Divisão por 0'
                    break
                else:
                    divisao = int(operacao[1]) // int(operacao[2])
                    return divisao
                    break
        print(divisao(operacao))
        if divisao(operacao) == 'Erro: Divisão por 0':
            break
    
    elif operacao[i] == '5':
        break
