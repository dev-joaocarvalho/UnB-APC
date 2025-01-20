'''
Você, e apenas você tem uma string s
 com n
 letras minúsculas entre "a" e "z".

Você tem que remover no máximo um (ou seja, nenhum ou um único caractere) caractere desta string de um modo que a string que você obtiver seja a menor lexicograficamente dentre todas as strings que podem ser obtidas a partir desta operação.

Uma string s=s1s2...sn
 é menor lexicograficamente que a string t=t1t2...tm
 se algum dos critérios abaixo for satisfeito:

se n<m
 e s1=t1,s2=t2,...,sn=tn
, ou;
se existe um número p
 tal que p≤min(n,m)
 e s1=t1,s2=t2,...,sp−1=tp−1
 e sp<tp
.
Por exemplo, "aaa" é menor que "aaaa", "abb" é menor que "abc" e "pqr" é menor que "z".



Entrada

A primeira linha contém um número n
, o tamanho de s
.

A segunda linha da entrada contém exatamente n
 letras minúsculas, a string s
.



Saída

Imprima uma string - a menor string lexicograficamente possível que pode ser obtida ao remover no máximo 1 caractere da string s
.  
'''
# Lê o tamanho da string
n = int(input())

# Lê a string
s = input().strip()

# Percorre a string para encontrar o primeiro caractere que deve ser removido
for i in range(n - 1):
    if s[i] > s[i + 1]:
        # Remove o caractere na posição i
        print(s[:i] + s[i+1:])
        break
else:
    # Se não encontrou nenhum caractere maior que o próximo, remove o último caractere
    print(s[:-1])
