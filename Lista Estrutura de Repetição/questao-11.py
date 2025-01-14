'''
Codifique um programa que leia uma quantidade n≥1
 de números e diga qual é o menor e qual é o maior valor.



Entrada
A primeira linha contém um inteiro n≥1
. As próximas n
 linhas contém inteiros −10^4≤x≤10^4
.



Saída
Imprima o menor e maior valores da sequência, como é mostrado nos exemplos. 
'''
 Lê a quantidade de números
n = int(input())

# Inicializa as variáveis para o menor e maior valor
menor = 10**5  # Maior valor possível do problema
maior = -10**5  # Menor valor possível do problema

# Lê os n números e determina o menor e maior
for _ in range(n):
    x = int(input())
    if x < menor:
        menor = x
    if x > maior:
        maior = x

# Imprime o menor e maior valor conforme o formato
print(f"Menor: {menor}")
print(f"Maior: {maior}")
