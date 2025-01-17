'''
Crie uma função soma_aninhada que receba uma lista de objetos L
 e retorna a soma de todos os elementos de todas as listas aninhadas. A lista L
 pode conter até 50
 objetos, que podem ser:

Números inteiros
Listas de números inteiros
Listas de listas de números inteiros
Entrada
Não há entrada. O parâmetro da função é uma lista de números.


Saída
A função deve retornar a soma dos elementos.
'''
def soma_aninhada(L):
    total = 0
    for item in L:
        if isinstance(item, int):  # Se for um número inteiro, adicionamos ao total
            total += item
        elif isinstance(item, list):  # Se for uma lista, chamamos a função recursivamente
            total += soma_aninhada(item)
    return total
