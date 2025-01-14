'''
Cedo ou tarde, você irá perceber que o ramo mais útil da matemática é a álgebra linear. Em alguns lugares, nem sequer utilizam o nome álgebra linear. Usam simplesmente matemática! Neste problema, você irá utilizar um pedacinho bem minúsculo da álgebra linear, voltado para geometria.
Na escola, nós aprendemos a determinar se um par de vetores bi ou tridimensionais é ortogonal (ou seja, se o ângulo entre os vetores é de 90o) calculando seu produto interno euclidiano:



                                                           u⋅v=xu⋅xv+yu⋅yv     (para 2 dimensões - bidimensionais)

                                                                                                    ou

                                                           u⋅v=xu⋅xv+yu⋅yv+zu⋅zv
      (para 3 dimensões - tridimensionais)



Dois vetores u
 e v
 são ortogonais se, e somente se, u⋅v
 = 0. Neste problema, você deve determinar se um dado par de vetores n
-dimensionais u
 e v
 é ortogonal.



Entrada
A primeira linha da entrada contém um único inteiro n
  ( 1≤n≤10^5
 ), que indica a dimensão dos vetores a serem lidos, ou seja, o número de coordenadas cartesianas de um vetor.

A segunda linha contém n
 inteiros ui
 (−100≤ui≤100
) separados por espaço, que são as n
 coordenadas do vetor u
.

A terceira linha contém n
 inteiros vi
 (−100≤vi≤100
) separados por espaço, que são as n
 coordenadas do vetor v
.

Saída
Se os vetores u
 e v
 forem ortogonais, imprima a mensagem "ortogonais" (sem aspas duplas). Caso contrário, imprima o valor do produto interno euclidiano entre eles.



Observação
Para ler as n coordenadas de um vetor em uma única linha, basta utilizar o seguinte código:

vet = list(map(int,input().strip().split()))[:n]
'''
# Lê a dimensão n
n = int(input())

# Lê os vetores u e v
u = list(map(int, input().strip().split()))
v = list(map(int, input().strip().split()))

# Calcula o produto escalar (produto interno)
produto_interno = sum(u[i] * v[i] for i in range(n))

# Verifica se os vetores são ortogonais
if produto_interno == 0:
    print("ortogonais")
else:
    print(produto_interno)
