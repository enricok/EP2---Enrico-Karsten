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

def posiciona_frota (frota):
    tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]       
    for navio, valor in frota.items():
        for coordenadas in valor:
            for chave in coordenadas:
                tabuleiro [chave[0]][chave[1]] = 1
    return tabuleiro

def afundados (frota, tabuleiro):
    count = 0
    entrou = 0
    quantos_afundaram = 0
    for navio, valor in frota.items():
        for coordenadas in valor:
            for chave in coordenadas:
                if tabuleiro [chave [0]][chave[1]] == "X":
                    entrou += 1
                count += 1
            if count == entrou:
                quantos_afundaram += 1
                count = 0
                entrou = 0
            else:
                count = 0
                entrou = 0
    return quantos_afundaram

def posicao_valida (frota, linha, coluna, orientacao, tamanho):
    resposta = True
    barco = define_posicoes (linha, coluna, orientacao, tamanho)
    if frota == {}:
        for coordinates in barco:
            if coordinates [0] > 9:
                resposta = False
            if coordinates [1] > 9:
                resposta = False      
    else:
        for navio, valor in frota.items():
            for coordenadas in valor:
                for chave in coordenadas:
                    for coordinates in barco:
                        if chave [0] == coordinates [0] and chave [1] == coordinates [1]:
                            resposta = False 
                        if coordinates [0] > 9:
                            resposta = False
                        if coordinates [1] > 9:
                            resposta = False
        for coordinates in barco:
            if coordinates [0] > 9:
                resposta = False
            if coordinates [1] > 9:
                resposta = False              
    return resposta

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto