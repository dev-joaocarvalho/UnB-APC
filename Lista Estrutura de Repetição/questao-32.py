'''
Defina a função remove_duplicatas, que recebe uma lista e retorna uma nova lista com os mesmos elementos e na mesma ordem, mas sem valores duplicados.



Entrada
Não há entrada. O parâmetro da função é uma lista de números.



Saída
A função deve retornar uma lista sem elementos duplicados.
'''
def remove_duplicatas(lista):
    resultado = []  # Lista para armazenar os elementos sem duplicatas
    vistos = set()  # Conjunto para rastrear elementos já adicionados

    for item in lista:
        if item not in vistos:
            resultado.append(item)  # Adiciona à lista de resultado
            vistos.add(item)  # Marca como "visto"
    
    return resultado
