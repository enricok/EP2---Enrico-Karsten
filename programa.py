frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}     

navios = ["porta-aviões", "navio-tanque", "contratorpedeiro", "submarino"]

for navio in navios:
    i = 0
    if navio == "porta-aviões":
        quantidade = 1
    if navio == "navio-tanque":
        quantidade = 2
    if navio == "contratorpedeiro":
        quantidade = 3
    if navio == "submarino":
        quantidade = 4

    while i < quantidade:
            
        if navio == "porta-aviões":
            tamanho = 4

        if navio == "navio-tanque":
            tamanho = 3

        if navio == "contratorpedeiro":
            tamanho = 2

        if navio == "submarino":
            tamanho = 1
            
        print (f"Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}")

        if navio == "submarino":
            linha = int(input ("Qual é a linha? "))
            coluna = int (input ("Qual é a coluna? "))
        else:
            linha = int(input ("Qual é a linha? "))
            coluna = int (input ("Qual é a coluna? "))
            orientacao = int (input ("Qual é a orientação (1 - veritcal; 2 - horizontal)? "))

        if orientacao == 1:
            orientacao = "vertical"

        if orientacao == 2:
            orientacao = "horizontal"

        boolean = posicao_valida (frota, linha, coluna, orientacao, tamanho)

        if boolean == False:
            print ("Esta posição não está válida!")
            while boolean == False:
                print (f"Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}")
                if navio == "submarino":
                    linha = int(input ("Qual é a linha? "))
                    coluna = int (input ("Qual é a coluna? "))
                else:
                    linha = int(input ("Qual é a linha? "))
                    coluna = int (input ("Qual é a coluna? "))
                    orientacao = int (input ("Qual é a orientação (1 - veritcal; 2 - horizontal)? "))
                if orientacao == 1:
                    orientacao = "vertical"
                if orientacao == 2:
                    orientacao = "horizontal"
                boolean = posicao_valida (frota, linha, coluna, orientacao, tamanho)
                if boolean == False:
                    print ("Esta posição não está válida!")

        if boolean == True:
            barco = define_posicoes (linha, coluna, orientacao, tamanho)
            frota = preenche_frota (frota, navio, linha, coluna, orientacao, tamanho)
        i += 1

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota (frota_oponente)

tabuleiro_jogador = posiciona_frota (frota)

jogando = True

count = 0

for navio, valor in frota_oponente.items():
    for coordenadas in valor:
        count += 1

lista = []

while jogando == True:

    tabuleiro_pronto = monta_tabuleiros (tabuleiro_jogador, tabuleiro_oponente)
        
    print (tabuleiro_pronto)

    linha = int(input ("Jogador, qual linha deseja atacar? "))

    while linha < 0 or linha > 9:
        print ('Linha inválida!')
        linha = int(input ("Jogador, qual linha deseja atacar? "))

    coluna = int(input ("Jogador, qual coluna deseja atacar? "))

    while coluna < 0 or coluna > 9:
        print ('Coluna inválida!')
        coluna = int(input ("Jogador, qual coluna deseja atacar? "))

    while [linha, coluna] in lista:
        print (f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        linha = int(input ("Jogador, qual linha deseja atacar? "))

        while linha < 0 or linha > 9:
            print ('Linha inválida!')
            linha = int(input ("Jogador, qual linha deseja atacar? "))

        coluna = int(input ("Jogador, qual coluna deseja atacar? "))

        while coluna < 0 or coluna > 9:
            print ('Coluna inválida!')
            coluna = int(input ("Jogador, qual coluna deseja atacar? "))

    lista.append ([linha, coluna])

    tabuleiro_oponente = faz_jogada (tabuleiro_oponente, linha, coluna)

    quantos_afundaram = afundados (frota_oponente, tabuleiro_oponente)

    if count == quantos_afundaram:
        print ("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
        break