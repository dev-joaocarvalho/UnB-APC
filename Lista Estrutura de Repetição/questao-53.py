'''
Pedra, papel e tesoura, também chamado em algumas regiões do Brasil de jokenpô é um jogo de mãos recreativo e simples para duas ou mais pessoas, que não requer equipamentos nem habilidade. No jokenpô, os jogadores devem simultaneamente esticar a mão, na qual cada um formou um símbolo (que significa pedra, papel ou tesoura). Então, os jogadores comparam os símbolos para decidir quem ganhou, da seguinte forma: Pedra ganha da tesoura (porque pedra quebra tesoura); Tesoura ganha do papel (porque tesoura picota papel); e Papel ganha da pedra (porque papel embrulha pedra - é isso mesmo!!).

Assim, sua tarefa neste exercício é implementar esse jogo para dois jogadores.



Entrada

A entrada consiste de N
 (1≤N≤50
) casos de teste. N
 deve ser lido na primeira linha da entrada. Cada caso de teste é composto por uma linha contendo duas strings separadas por um espaço. A primeira string representa o sinal escolhido pelo jogador 1
 e a segunda string representa o sinal escolhido pelo jogador 2
. Essas strings podem ser:

"tesoura": para representar a Tesoura;
"pedra": para representar a Pedra;
"papel": para representar o Papel.


Saída

A saída deve conter o seguinte:

"Jogador 01 venceu.": se o Jogador 1
 tiver vencido a partida;
"Jogador 02 venceu.": se o Jogador 2
 tiver vencido a partida;
"Empate." .
Cada saída de um caso de teste deve estar em uma linha.
'''
def jokenpo(jogador1, jogador2):
    if jogador1 == jogador2:
        return "Empate."
    elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
         (jogador1 == "tesoura" and jogador2 == "papel") or \
         (jogador1 == "papel" and jogador2 == "pedra"):
        return "Jogador 01 venceu."
    else:
        return "Jogador 02 venceu."

N = int(input())
for _ in range(N):
    jogador1, jogador2 = input().split()
    print(jokenpo(jogador1, jogador2))
