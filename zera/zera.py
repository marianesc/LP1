def zera_acima_ou_abaixo(m):
    diagonal = 0
    acima = 0
    abaixo = 0
    for ilin in range(len(m)):
        for icol in range(len(m[0])):
            if icol > ilin:
                acima += m[ilin][icol]
            elif icol < ilin:
                abaixo += m[ilin][icol]

    if acima > abaixo:
        for ilin in range(len(m)):
            for icol in range(len(m[0])):
                if icol > ilin:
                    m[ilin][icol] = 0

    elif abaixo > acima:
        for ilin in range(len(m)):
            for icol in range(len(m[0])):
                if icol < ilin:
                    m[ilin][icol] = 0

    elif abaixo == acima:
        for ilin in range(len(m)):
            for icol in range(len(m[0])):
                if icol < ilin or icol > ilin:
                    m[ilin][icol] = 0


