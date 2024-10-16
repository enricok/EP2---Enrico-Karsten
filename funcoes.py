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

def preenche_frota (frota, nome, linha, coluna, orientacao, tamanho):
    posicao = define_posicoes (linha, coluna, orientacao, tamanho)
    if nome in frota:
        frota [nome].append (posicao)
    else:
        frota [nome] = [posicao]
    return frota

def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro [linha][coluna] == 1:
        tabuleiro [linha] [coluna] = "X"
    if tabuleiro [linha][coluna] == 0:
        tabuleiro [linha][coluna] = "-"
    return tabuleiro

    
        