'''
Ajude a escrever funções para o Jogo da Velha. 

Neste exercício, o jogo sempre começará com o jogador (X) e ambos os jogadores devem efetuar seus lances de forma alternada. Após cada lance, o tabuleiro deve ser atualizado. Ajude a construir esse jogo implementado somente a seguinte função:

Funcao que testa se a partida terminou
def jogoTerminou(matriz):




Entrada
Não há entrada. O parâmetro da função é uma matriz de caracteres representando o tabuleiro e suas jogadas. 


Saída
A função deve retornar o estado de checagem do tabuleiro sendo 0, caso a partida não tenha terminado, 1 caso a haja um vencedor (independente de quem) e 2 caso a partida tenha terminado em empate.


Observação
Espaços não preenchidos da matriz contém o símbolo hífen (-) e pode ser vista dessa forma:

 -  -  - 
 -  -  - 
 -  -  - 
Durante a partida a matriz é populada com as letras X (xis maiúsculo) e O (o maiúsculo), e impressa como neste exemplo:
 X  O  X 
 O  X  O 
 X  -  X
'''
def jogoTerminou(matriz):
    # Verificação de vitória: Linhas, Colunas e Diagonais
    for i in range(3):
        # Verificar linha i
        if matriz[i][0] == matriz[i][1] == matriz[i][2] and matriz[i][0] != ' - ':
            return 1
        # Verificar coluna i
        if matriz[0][i] == matriz[1][i] == matriz[2][i] and matriz[0][i] != ' - ':
            return 1

    # Verificar diagonais
    if matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] != ' - ':
        return 1
    if matriz[0][2] == matriz[1][1] == matriz[2][0] and matriz[0][2] != ' - ':
        return 1

    # Verificação de empate: Não há espaços vazios e não há vencedor
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == ' - ':
                return 0  # Se houver espaço vazio, o jogo não terminou

    # Se não houver espaços vazios e ninguém venceu, então é empate
    return 2
