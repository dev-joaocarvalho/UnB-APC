'''
Alice e Bob são personagens lendários usados para apresentar de maneira didática situações onde há uma comunicação entre duas entidades A e B.

Imagine que Bob deseja enviar uma imagem para Alice. Na Internet, isto é feito quebrando a imagem em vários pedaços, chamados de datagramas, e enviando um datagrama de cada vez. O problema é que os datagramas podem se espalhar por diferentes caminhos para chegarem ao seu destino. Deste modo, os datagramas podem chegar desordenados ao computador de Alice. Para evitar esta confusão, os datagramas são enviados por Bob com um número de sequência. Bob sempre envia um datagrama com um número de sequência maior que o número de sequência do datagrama que foi enviado por último.

Desta maneira, Alice pode reconstruir a imagem simplesmente ordenando os datagramas que ela recebeu, pelos respectivos números de sequência. Mas antes de fazer isto, Alice te pediu ajuda para calcular um número.

Ela quer saber quantas inversões aconteceram no envio da imagem. O número de inversões é o número de pares {Si,Sj}
 tais que i<j
 e Si>Sj
 onde S1
 é o número de sequência do datagrama que chegou primeiro, S2
 é o número de sequência do datagrama que chegou em segundo lugar, S3
 é o número de sequência do datagrama que chegou em terceiro lugar, e assim por diante.



Entrada
A primeira e única linha contém uma sequência de N
 ( 1≤N≤10^3
 ) inteiros não-negativos Si(1≤Si≤10^9)
 que são os números de sequência dos datagramas em ordem de chegada ao computador de Alice.



Saída
Imprima uma linha com o número de inversões, como descrito no enunciado (o número de pares tais que i<j
 e Si>Sj
 ).
'''
def merge_count_split_inv(arr, temp_arr, left, right):
    if left == right:
        return 0

    mid = (left + right) // 2
    inv_count = merge_count_split_inv(arr, temp_arr, left, mid)
    inv_count += merge_count_split_inv(arr, temp_arr, mid + 1, right)
    inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    return inv_count

def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Inicializa o índice para a sublista esquerda
    j = mid + 1 # Inicializa o índice para a sublista direita
    k = left    # Índice para a lista temporária
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1) # Todos os elementos restantes na sublista esquerda
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    
    return inv_count

def count_inversions(arr):
    n = len(arr)
    temp_arr = [0] * n
    return merge_count_split_inv(arr, temp_arr, 0, n - 1)

# Leitura da entrada
arr = list(map(int, input().split()))

# Contagem de inversões
result = count_inversions(arr)

# Imprime o resultado
print(result)
