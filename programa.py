navios = ["porta-aviões", "navio-tanque", "contratorpedeiro", "submarino"]

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
    }   

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

print (frota)
