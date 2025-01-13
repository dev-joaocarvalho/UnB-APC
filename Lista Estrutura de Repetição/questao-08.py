'''
Dois números inteiros são co-primos, ou primos entre si, se seu único divisor inteiro em comum é a unidade. Isto é, o máximo divisor comum entre os dois números é 1.

Escreva um programa que verifique se dois números são co-primos.



Entrada
A entrada consiste de dois números inteiros naturais, separados por espaço, ambos maiores que 1.



Saída
A saída deve ser uma mensagem indicando a decisão de co-primalidade sobre os números, conforme os exemplos.
 '''
# Função que calcula o MDC usando o Algoritmo de Euclides
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Leitura da entrada
a, b = map(int, input().split())

# Verificação se são co-primos
if mdc(a, b) == 1:
    print("Sao co-primos.")
else:
    print("Nao sao co-primos!")
