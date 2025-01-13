'''
"Um dragão, dois dragões, três dragões" - a princesa contava. 

Entretanto, só contar dragões para tentar dormir também era chato, então ela se entretia o melhor que podia. Uma noite ela imaginou que todos os dragões tentavam roubá-la e ela estava lutando para se salvar. 

Toda vez que ela contar k dragões, o dragão é socado na cara com uma frigideira. Toda vez que ela contar I dragões, o dragão tem seu rabo preso na porta. Toda vez que ela contar m dragões, o dragão tem suas patas pisoteadas por salto alto. Por último, sempre que ela contar n dragões, ela tranca o dragão na geladeira.

Quantos dragões imaginários sofreram dano físico ou moral se a princesa contou um total de d
 dragões?

No primeiro exemplo mostrado abaixo, como a princesa deve contar de 1 a 12, e esses valores são divisíveis por 1, 2, 3 e 4 então, foram 12 dragões que sofreram dano.

Entrada
A entrada contém os números k
, l
, m
, n
 e d
, cada número em uma linha diferente. 1≤k,l,m,n≤10,1≤d≤105
.



Saída
Imprima o número de dragões machucados.
'''
# Lendo os valores
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

# Conjunto para armazenar os dragões danificados
damaged_dragons = set()

# Iterando sobre os dragões de 1 até d
for i in range(1, d + 1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        damaged_dragons.add(i)

# A resposta é o número de dragões danificados
print(len(damaged_dragons))

