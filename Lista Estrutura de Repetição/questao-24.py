'''
Dado um conjunto de números de inteiros X={x1,x2,…,xN}
, a variância (σ2
) de X
 é dada por:

σ2=∑i=1N(xi−x¯)2N
,

em que x¯
 representa a média de X
. Além disso, o desvio padrão (σ
) pode ser descrito por:

σ=∑i=1N(xi−x¯)2N−−−−−−−√


que nada mais é do que a raiz quadrada da variância. Dessa forma, escreva um programa para calcular a variância e o desvio padrão de X
.




Entrada
A entrada consiste de N
 ( 1≤N≤100
 ) números inteiros x1,x2,…,xN
 (−103≤xi≤103,i=1,…,N
) separados por espaço em branco.



Saída
Imprima duas linhas, em que cada uma contém um valor em ponto flutuante com uma casa decimal de precisão. A primeira linha deve apresentar a variância de X
, enquanto que a segunda linha deve apresentar o desvio padrão de X
.
'''
import math

# Função para calcular a variância e o desvio padrão
def calcular_variancia_e_desvio(X):
    # Calculando a média
    n = len(X)
    media = sum(X) / n
    
    # Calculando a variância
    variancia = sum((xi - media) ** 2 for xi in X) / n
    
    # Calculando o desvio padrão
    desvio_padrao = math.sqrt(variancia)
    
    return variancia, desvio_padrao

# Leitura da entrada
X = list(map(int, input().split()))

# Calcular a variância e o desvio padrão
variancia, desvio_padrao = calcular_variancia_e_desvio(X)

# Imprimir os resultados com uma casa decimal
print(f"{variancia:.1f}")
print(f"{desvio_padrao:.1f}")
