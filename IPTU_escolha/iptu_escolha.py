#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#IPTU ESCOLHENDO FORMA DE PAGAMENTO

area = float(input())
valor = float(input())
pagamento = input()

imposto = area * valor

desconto = 0
parcelas = 0
valor_final = 0

if pagamento == 'vista':
    desconto = 0.2 * imposto
    valor_final = imposto - desconto
    print('Total: R$ {:.2f}'.format(valor_final))
elif pagamento == '2x':
    desconto = 0.1 * imposto
    valor_final = imposto - desconto
    parcelas =  valor_final / 2
    print('Total: R$ {:.2f}. Parcelas: R$ {:.2f}'.format(valor_final,parcelas))
elif pagamento == '3x':
    desconto = 0.05 * imposto
    valor_final = imposto - desconto
    parcelas = valor_final / 3
    print('Total: R$ {:.2f}. Parcelas: R$ {:.2f}'.format(valor_final,parcelas))
