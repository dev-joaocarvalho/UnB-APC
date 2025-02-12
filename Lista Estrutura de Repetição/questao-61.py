'''
Uma palavra foi comprimida para um número inteiro utilizando o seguinte algoritmo:

Cada letra maiúscula de 'A' até 'Z' foi mapeada para um número entre 1
 e 26
, sendo a letra 'A' representada pelo número 1
, a letra 'B' pelo número 2
 e assim por diante.
O valor da primeira letra da palavra foi colocado nos 5
 primeiros bits do inteiro, os menos significativos. A segunda letra foi colocado nos próximos 5
 bits e assim por diante, até a última letra da palavra.
Depois de colocar cada letra no número inteiro, os bits restantes desse número foram deixados como 0
.
Sua tarefa é recuperar a palavra original dado o inteiro que a representa. Para isso, escreva a função decompress(x)
 que recebe como parâmetro o inteiro x
 e retorna a palavra original.



Entrada
O único parâmetro da sua função será o valor 0≤x≤2.109
, a versão comprimida da palavra.




Saída
A função deve retornar uma string: a palavra original que o inteiro x
 representa.



Notas
Considere a utilização das funções chr e ord.
'''
def decompress(x):
    word = ""
    
    # Enquanto o valor de x for maior que 0
    while x > 0:
        # Extrai os 5 bits menos significativos
        letter_value = x & 31  # 31 é 11111 em binário, que extrai 5 bits
        # Converte o valor para a letra correspondente
        letter = chr(letter_value + 64)  # 'A' começa em 1, então somamos 64 para obter o código ASCII
        # Adiciona a letra ao final da palavra
        word = word + letter
        # Desloca os bits 5 posições à direita para a próxima letra
        x >>= 5
    
    return word


