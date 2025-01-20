'''
Você, e apenas você, tem uma string s
 em que os caracteres são ou 0 ou 1.

Você quer que todos os 1's da string formem uma sequência contínua. Por exemplo, se a string é 0, 1, 00111 ou 01111100, então todos os 1's formam uma sequência contínua. Se a string for 0101, 100001 ou 111111111101, então a condição não é satisfeita.

Você pode apagar alguns (ou nenhum se quiser) 0's (zeros) da string. Qual o menor número de 0's que você tem que apagar para que a string da entrada tenha a condição satisfeita? 



Entrada

A primeira linha contém um número n
, quantas strings você terá que responder.

As próximas n
 linhas contém uma string s
 de tamanho entre 1
 e 100
 caracteres, onde cada caractere é ou 0
 ou 1
.



Saída

Imprima n
 inteiros, onde o i-ésimo inteiro é a resposta para a i-ésima string da entrada.
 '''
  # Número de casos de entrada
n = int(input())

# Para cada caso
for _ in range(n):
    s = input().strip()
    
    # Verificar se existe algum '1' na string
    if '1' not in s:
        print(0)
    else:
        # Encontrar o índice do primeiro e último '1'
        primeiro_1 = s.find('1')
        ultimo_1 = s.rfind('1')
        
        # Contar os '0's entre o primeiro e o último '1'
        zeros_a_remover = s[primeiro_1:ultimo_1+1].count('0')
        
        # Imprimir a quantidade de zeros a serem removidos
        print(zeros_a_remover)
