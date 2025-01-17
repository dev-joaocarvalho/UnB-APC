'''
Gabriel fez um jogo que salva em um vetor a pontuação que cada participante. Ele quer mostrar as pontuações em ordem reversa mas, como não sabe quantos jogadores existem, pediu que você fizesse um programa para ajudá-lo.



Entrada
A entrada consiste de uma linha com uma sequência de valores inteiros pi(1≤pi≤10^4)
 referentes a pontuação de cada jogador i(1≤i≤10^4)
. A sequência termina com um valor negativo (que não é uma pontuação válida).



Saída
Apresente, em uma linha, todas as pontuações já feitas, separadas por um espaço, na ordem reversa à de entrada.
'''
# Função para ler as pontuações e imprimir em ordem reversa
def mostrar_pontuacoes_reversas():
    # Ler a entrada
    pontuacoes = list(map(int, input().split()))
    
    # Remover o último elemento negativo da lista
    pontuacoes = [p for p in pontuacoes if p >= 0]
    
    # Imprimir as pontuações em ordem reversa
    print(" ".join(map(str, pontuacoes[::-1])))

# Chamada da função para executar o programa
mostrar_pontuacoes_reversas()
