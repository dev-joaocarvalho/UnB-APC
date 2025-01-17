'''
Ajude a escreva um programa para jogar o Jogo da Velha. Neste exercício, o jogo sempre começará com o jogador (X) e ambos os jogadores devem efetuar seus lances de forma alternada. Após cada lance o programa deverá imprimir o tabuleiro. Ao final da partida, o programa deverá mostrar uma mensagem indicando se ocorreu vitória ou empate e encerrar o programa. Utilizando as funções implementadas nas etapas anteriores, construa um programa de jogo da velha. 

Entrada 
Ler um par de número inteiros (linha, coluna) informando as coordenadas do lance 0≤l,c≤2
. 



Saída
A matriz contendo o estado do tabuleiro deverá ser impressa na tela de forma que cada item da matriz seja precedido e sucedido por um espaço em branco. 



Observação
A matriz inicial vazia deverá ser preenchida com o símbolo hífen (-) e impressa desta forma:



 -  -  - 
 -  -  - 
 -  -  - 
Durante a partida a matriz deverá ser populada com as letras X (xis maiúsculo) e O (o maiúsculo), e impressa como neste exemplo:

 X  O  X 
 O  X  O 
 X  -  X
'''
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(f" {celula}" for celula in linha))

def verificar_vitoria(tabuleiro):
    # Verificar linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != '-':
            return True
    
    # Verificar colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != '-':
            return True
    
    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != '-':
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != '-':
        return True
    
    return False

def verificar_empate(tabuleiro):
    # Verifica se ainda existem espaços vazios ('-')
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == '-':
                return False
    return True

def jogo_da_velha():
    # Inicializar o tabuleiro com '-' (vazio)
    tabuleiro = [['-' for _ in range(3)] for _ in range(3)]
    
    # Jogadores
    jogador_atual = 'X'
    
    # Iniciar o jogo
    while True:
        # Imprimir o tabuleiro
        imprimir_tabuleiro(tabuleiro)
        
        # Ler a coordenada do jogador atual
        linha, coluna = map(int, input().split())
        
        # Verificar se a posição está vazia
        if tabuleiro[linha][coluna] != '-':
            print("Posição ocupada, tente novamente.")
            continue
        
        # Fazer o movimento
        tabuleiro[linha][coluna] = jogador_atual
        
        # Verificar se há vitória
        if verificar_vitoria(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Ganhou")
            break
        
        # Verificar se há empate
        if verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate")
            break
        
        # Trocar o jogador
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Iniciar o jogo
jogo_da_velha()
