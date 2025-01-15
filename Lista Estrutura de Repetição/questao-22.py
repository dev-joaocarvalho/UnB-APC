'''
Escreva um programa que receba como entrada n
 1≥n≥100
 elementos de uma lista, e como saída, imprima True caso exista algum elemento que apareça mais de uma vez, e False caso contrário.

Entrada
Uma lista de números.


Saída
True ou False dependendo da existência ou não de elementos repetidos.
'''
def verificar_repetidos(lista):
    elementos = set()  # Conjunto para armazenar elementos únicos
    for numero in lista:
        if numero in elementos:
            return True  # Encontrou um número repetido
        elementos.add(numero)
    return False  # Não encontrou repetições

# Leitura da entrada
lista = list(map(int, input().split()))

# Chama a função e imprime o resultado
print(verificar_repetidos(lista))
