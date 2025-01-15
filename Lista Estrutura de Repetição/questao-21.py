'''
Palmério está treinando para uma meia maratona e todos os domingos realiza seus treinos em uma pista de atletismo, que possui formato oval e comprimento de 400 metros. Nesse treino, ele percorre N
 voltas na pista e registra o tempo gasto (em segundos) para percorrer cada uma dessas voltas.

Ao retornar para casa, Palmério estuda seu desempenho no treino da seguinte maneira: ele identifica o maior tempo tmax
 registrado para completar uma volta. Em seguida, ele analisa, volta a volta, o quanto ele foi mais rápido em cada volta em relação ao tempo tmax
.

Como Palmério pode ter percorrido várias voltas nessa pista, pode ser difícil fazer essas contas manualmente e, por isso, ele pede sua ajuda. Escreva um programa que calcule a diferença de tempo entre cada volta e o tempo tmax
.

Entrada
A primeira linha da entrada contém um número inteiro N
 (1≤N≤100
) indicando a quantidade de voltas percorridas na pista por Palmério em um treino. A segunda linha da entrada contém N
 inteiros separados por espaço em branco a1,a2,…,aN
, em que ai
 (1≤ai≤300
) indica o tempo (em segundos) percorrido por Palmério na i
-ésima volta.



Saída
Imprima N
 números inteiros separados por espaço em branco b1,b2,…,bN
, em que bi
 é a diferença de tempo entre a volta i
 e tmax
 e bi≥0
.
'''
# Leitura da entrada
N = int(input())  # Quantidade de voltas
tempos = list(map(int, input().split()))  # Lista de tempos de cada volta

# Encontrar o tempo máximo
tmax = max(tempos)

# Calcular as diferenças
diferencas = [tmax - tempo for tempo in tempos]

# Imprimir as diferenças
print(" ".join(map(str, diferencas)))
