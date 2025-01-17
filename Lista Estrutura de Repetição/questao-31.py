'''
Jonathan achou outra caixa com mais de seus chinelos velhos em sua casa, e decidiu dar para seu irmãozinho Bill todos os pares que ainda irão caber em seus pés e doar o restante. Para escolher o chinelo, Jonathan os enfileirou em ordem crescente de tamanho em sua frente e procurou o primeiro que era do tamanho certo ou maior do que o que seu irmão atualmente calça, já que ele ainda irá crescer.



Entrada
A primeira linha apresenta um inteiro T
 ( 15≤T≤40
 ), que representa quanto Bill calça. Na segunda linha são dados N
 ( 1≤N≤10
 ) inteiros, separados por espaço, cada um representando o tamanho de um chinelo na caixa velha. Os chinelos estão desordenados na caixa.



Saída
Uma linha com um inteiro que representa a posição do primeiro chinelo que cabe no pé de Bill. Caso não exista, imprima -1.



Observação
Jonathan sempre conta seus chinelos iniciando em 0. 

Ordene a lista de tamanhos (veja a função sort() disponível nas variável do tipo lista). 

'''
def encontrar_chinelo(T, chinelos):
    # Ordena a lista de chinelos em ordem crescente
    chinelos.sort()
    
    # Itera pela lista de chinelos e verifica qual o primeiro que serve para Bill
    for i in range(len(chinelos)):
        if chinelos[i] >= T:
            return i  # Retorna a posição do chinelo que serve para Bill
    
    # Caso nenhum chinelo sirva, retorna -1
    return -1

# Leitura da entrada
T = int(input())  # Tamanho do pé de Bill
chinelos = list(map(int, input().split()))  # Lista de tamanhos dos chinelos

# Chama a função e imprime o resultado
print(encontrar_chinelo(T, chinelos))
