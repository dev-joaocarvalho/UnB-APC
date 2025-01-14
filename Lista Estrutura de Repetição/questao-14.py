'''
Codifique um software que mostre "primo", para um número primo e "regular" para um número não primo.


Entrada
A única linha de entrada contém um inteiro  1<n≤10^5
. O ano em que Emidio nasceu.



Saída
Imprima "primo", se o número for primo e "regular", se o numero não for primo.
'''
import math

# Lê o número
n = int(input())

# Função para verificar se o número é primo
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Verifica se o número é primo e imprime o resultado
if eh_primo(n):
    print("primo")
else:
    print("regular")
