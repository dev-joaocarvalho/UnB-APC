'''
Gabriel fez um joguinho que salva em uma lista a quantidade de pontos que cada participante fez. Ele quer saber a menor e maior pontuação já feita, e pediu que você fizesse um programa para ajudá-lo.



Entrada
A entrada consiste de uma linha com N
 valores inteiros referentes a pontuação pi(−10≤pi≤10000)
 de cada jogador i
. É garantido que não há pontuações iguais.



Saída
Apresente, na primeira linha, o valor da menor pontuação obtida por um jogador e o inteiro referente a sua posição no vetor, separados por um espaço. Na segunda linha, apresente o valor inteiro referente a maior pontuação e o inteiro referente a sua posição no vetor, separados por um espaço. Na terceira linha, todas as pontuações já feitas, separadas por um espaço, exatamente na ordem da entrada.
'''
# Função para encontrar a menor e maior pontuação e suas posições
def pontuacoes():
    # Ler a entrada
    pontuacoes = list(map(int, input().split()))
    
    # Encontrar a menor pontuação e sua posição
    menor_pontuacao = min(pontuacoes)
    pos_menor = pontuacoes.index(menor_pontuacao)
    
    # Encontrar a maior pontuação e sua posição
    maior_pontuacao = max(pontuacoes)
    pos_maior = pontuacoes.index(maior_pontuacao)
    
    # Imprimir os resultados
    print(menor_pontuacao, pos_menor)
    print(maior_pontuacao, pos_maior)
    print(" ".join(map(str, pontuacoes)))

# Chamada da função para executar o programa
pontuacoes()
