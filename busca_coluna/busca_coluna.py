def busca_todos_por_coluna_em_matriz(m, e):
    local = []
    for icol in range(len(m[0])):
        for ilin in range(len(m)):
            if e == m[ilin][icol]:
                local.append((ilin, icol))

    return local

