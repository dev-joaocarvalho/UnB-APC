'''
Codifique um software que leia uma quantidade desconhecida de valores e informe a média aritmética



Entrada
A entrada é composta por um número 2≤n≤10^6
 desconhecido de linhas. Cada linha indica um valor  0≤x≤10^3
  a ser considerado para a média, exceto a última, que contém somente o número -1 para indicar que não há mais valores a serem lidos.




Saída
Escreva um programa que leia a entrada e imprima a parte inteira da média aritmética.



Notas
O valor −1
 não deve ser considerado para a média.
'''
# Inicializa as variáveis para soma e quantidade de valores
soma = 0
quantidade = 0

# Lê os valores até encontrar -1
while True:
    x = int(input())
    
    # Se o valor for -1, encerra a leitura
    if x == -1:
        break
    
    # Adiciona o valor à soma e incrementa a quantidade
    soma += x
    quantidade += 1

# Calcula a média aritmética e imprime a parte inteira
if quantidade > 0:
    media = soma // quantidade  # Divisão inteira para pegar apenas a parte inteira
    print(media)
