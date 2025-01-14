'''
Codifique um software que leia n vetores de forças direcionada a um corpo e verifique se o mesmo encontra-se estacionário.



Entrada
A primeira linha contém um inteiro  1≤n≤100
 representando o número de vetores. Depois, há n
 linhas contendo 3 inteiros cada: as coordenadas xi
, yi
, e zi
 do vetor de forças i
 aplicado ao corpo.



Saída
A saída deve conter uma única linha com  ESTACIONARIO se o corpo está estacionário ou MOVIMENTO caso contrário.
'''
# Lê o número de vetores
n = int(input())

# Inicializa as somas das componentes em x, y e z
soma_x, soma_y, soma_z = 0, 0, 0

# Processa cada vetor de força
for _ in range(n):
    x, y, z = map(int, input().split())
    soma_x += x
    soma_y += y
    soma_z += z

# Verifica se a soma das forças é zero em todas as direções
if soma_x == 0 and soma_y == 0 and soma_z == 0:
    print("ESTACIONARIO")
else:
    print("MOVIMENTO")
