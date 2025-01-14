'''
Codifique um software que leia uma quantidade desconhecida de valores e informe a média harmônica.



Entrada
A entrada é composta por um número 2≤n≤10^6
 desconhecido de linhas. Cada linha indica um valor  0≤x≤10^3
  a ser considerado para a média, exceto a última, que contém somente o número -1 para indicar que não há mais valores a serem lidos.



Saída
Escreva um programa que leia a entrada e imprima a parte inteira da média aritmética.



Notas
O valor −1
 não deve ser considerado para a média harmônica.
'''
# Inicializando a soma dos inversos e a contagem dos valores
soma_inversos = 0
quantidade = 0

# Lê os valores até encontrar -1
while True:
    x = int(input())
    
    if x == -1:
        break
    
    # Soma os inversos dos valores
    soma_inversos += 1 / x
    quantidade += 1

# Calcula a média harmônica
if quantidade > 0:
    media_harmonica = quantidade / soma_inversos
    print(int(media_harmonica))  # Parte inteira da média harmônica
