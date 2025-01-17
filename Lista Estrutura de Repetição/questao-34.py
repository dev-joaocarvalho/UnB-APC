'''
Um conceito muito utilizado na Computação é o de soma de prefixos ou prefix sum. O prefix sum é um vetor que possui a soma cumulativa dos valores de um outro vetor, da seguinte forma: dada uma sequência de números x0,x1,x2,…
 e uma segunda sequência de números y0,y1,y2,…
, as somas de prefixos são dadas pelo seguinte:

y0=x0

y1=x0+x1


y2=x0+x1+x2


…

Assim, crie um algoritmo que receba um vetor de inteiros e retorne o vetor da soma de prefixos desse vetor.



Entrada
A primeira linha contém N
 ( 1≤N≤50
 ) números inteiros x1,x2,...,xN
 separados por espaço em branco, em que xi
 (0≤xi≤10000
 ) representa o valor da i-ésima posição desse vetor de inteiros.



Saída
Imprima na primeira linha o vetor com as somas de prefixos e na segunda linha o vetor de inteiros lido da entrada. Todos os valores dos vetores devem ser impressos separados por espaço.
'''
def soma_prefixos(vetor):
    soma_prefixo = []
    soma = 0
    for num in vetor:
        soma += num
        soma_prefixo.append(soma)
    return soma_prefixo

# Leitura da entrada
vetor = list(map(int, input().split()))

# Calculando a soma de prefixos
prefixos = soma_prefixos(vetor)

# Imprimindo os resultados
print(" ".join(map(str, prefixos)))
print(" ".join(map(str, vetor)))
