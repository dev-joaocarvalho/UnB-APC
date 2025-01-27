'''
Ianerisson tem uma string s
 com apenas letras minúsculas de 'a' a 'z'. Ele quer trocar exatamente um caractere de modo que a nova string seja um palíndromo.

Um palíndromo é uma string que possui a mesma sequência de caracteres, tanto de frente para trás, como de trás para frente. Por exemplo as strings "z", "aaa", "aba" e "abccba" são palíndromos, enquanto que as strings "codeforces", "realidade" e "ab" não são palíndromos.



Entrada

A primeira linha contém uma string s
 de até 100
 caracteres.



Saída

Imprima "ON" (sem as aspas duplas) se Ianerisson puder trocar exatamente um caractere para que a string resultante seja um palíndromo e "OFF" (sem as aspas duplas) caso contrário.
'''
def check_palindrome(s):
    n = len(s)
    count = 0
    
    # Verificamos os caracteres simétricos na string
    for i in range(n // 2):  # Só precisamos verificar até a metade da string
        if s[i] != s[n - i - 1]:
            count += 1
    
    # Se houver exatamente uma diferença, podemos corrigir com uma troca
    if count == 1 or (count == 0 and n % 2 == 1):
        return "ON"
    else:
        return "OFF"

# Entrada
s = input().strip()

# Saída
print(check_palindrome(s))
