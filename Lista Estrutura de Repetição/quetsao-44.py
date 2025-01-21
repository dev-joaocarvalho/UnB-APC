'''
Guilherme está entediado nessa quarentena e começa a brincar com a criação de substrings, de tamanhos variados, a partir de uma string inicial. Sabendo disso, você entra em contato com Guilherme e faz q
 consultas sobre possíveis substrings que podem ser geradas. Cada consulta contém dois números inteiros l
 e r
 e uma string s=s0s1…sn−1
, em que 0≤l≤r<n
 e si
 é um caractere alfanumérico. Para responder cada consulta, Guilherme deve gerar uma substring cujos caracteres estejam no intervalo [l,r]
 da string s
, isto é, slsl+1…sr−1sr
.

Sua tarefa consiste em gerar a resposta do Guilherme para cada consulta.



Entrada

A primeira linha da entrada contém um número inteiro q
 (1≤q≤100
), indicando a quantidade de consultas. As próximas q
 linhas descrevem todas essas consultas. Cada consulta é composta por dois números inteiros l
 e r
,  e por uma string s
, nessa ordem e separados por espaço em branco. A string s=s0s1…sn−1
, em que 1≤n≤100
, possui apenas caracteres alfanuméricos, e 0≤l≤r<n
.



Saída

Para cada consulta, imprima uma única linha - a substring resultante slsl+1…sr+1sr
.
'''
# Função para processar cada consulta e gerar a substring
def gerar_substring(l, r, s):
    # l e r são os índices da substring, e s é a string original
    return s[l:r+1]

# Leitura da quantidade de consultas
q = int(input())

# Para cada consulta, lemos os dados e processamos
for _ in range(q):
    # Lemos os números l, r e a string s
    l, r, s = input().split()
    l, r = int(l), int(r)
    
    # Geramos e imprimimos a substring correspondente
    print(gerar_substring(l, r, s))

