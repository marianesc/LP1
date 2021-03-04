def move_direita(labirinto):
    for ilin in range(len(labirinto)):
        for icol in range(len(labirinto[0])):
            if labirinto[ilin][icol] == '*' and icol != len(labirinto[0]) - 1:
                if labirinto[ilin][icol + 1] == ' ':
                    labirinto[ilin][icol], labirinto[ilin][icol +1] = labirinto[ilin][icol +1],labirinto[ilin][icol]
                    return (ilin, icol + 1)
                    break
                else:
                    return (ilin, icol)
                    break
            elif labirinto[ilin][icol] == '*' and icol == len(labirinto[0]) - 1:
                return (ilin, icol)
                break
