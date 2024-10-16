def define_posicoes (linha, coluna, orientacao, tamanho):
    barco = [[linha, coluna]]
    n = tamanho
    i = 1
    if orientacao == "vertical":
        while i < n:
            barco.append([linha + i, coluna])
            i += 1
    if orientacao == "horizontal":
        while i < n:
            barco.append([linha, coluna + i])
            i += 1
    return barco


    
        