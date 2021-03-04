#UFCG - PROG1
#MARIANE SILVA DE CARVALHO - 119210450
#CAIXA REGISTRADORA

#entrada: lista de valores reais representando as vendas e um número real que representa a meta
#saida: retornar outra lista com um relatório geral sobre o dia contendo a soma das vendas do dia, o total de comissões e a situação (lucro ou prejuízo)

def caixa_registradora(vendas, meta):
    soma = 0
    for venda in vendas:
        soma += venda

    comissoes = 0
    for venda in vendas:
        if venda < 1000:
            comissoes += venda * 0.05
        elif 1000 <= venda < 5000:
            comissoes += venda * 0.1
        elif venda >= 5000:
            comissoes += venda * 0.15

    if soma - comissoes >= meta:
        situacao = 'Lucro'
    else:
        situacao = 'Prejuizo'

    return [soma, comissoes, situacao]
