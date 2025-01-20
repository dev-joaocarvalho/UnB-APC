'''
A linguagem de programação clássica da UnBanda é a UnBit. A linguagem é peculiar e bastante complicada uma vez que só tem uma variável, chamada x
 e duas operações disponíveis:

Operação ++ aumenta o valor da variável x
 em 1.
Operação -- diminui o valor da variável x
 em 1.
Uma linha de código na UnBit consiste exatamente de uma operação e uma variável x
. A linha é escrita sem espaços, ou seja, só pode conter os caracteres +, - e X. Executar uma linha significa aplicar a operação que está nela e executar um programa significa interpretar todas as linhas desse programa.

Você recebe um programa em UnBit. O valor inicial de x
 é 0. Execute o programa e descubra o valor final da variável x
 depois que todas as linhas são executadas.



Entrada
O número n
 de linhas com as respectivas instruções do programa.



Saída
Um único inteiro - o valor final de x
'''
# Leitura do número de linhas do programa
n = int(input())

# Inicializando a variável x com valor 0
x = 0

# Processando cada linha de código
for _ in range(n):
    instrução = input().strip()
    if '++' in instrução:
        x += 1  # Se houver '++', incrementamos
    elif '--' in instrução:
        x -= 1  # Se houver '--', decrementamos

# Imprimimos o valor final de x
print(x)
    
