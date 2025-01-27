'''
Deivis está muito triste que muitas pessoas da interwebs misturam letras maiúsculas e minúsculas na mesma palavra. É por isso que ele inventou uma extensão para o seu browser favorito que iria mudar letras de todas as palavras de modo que cada palavra só tivesse ou letras minúsculas ou letras maiúsculas. Para ele, também é importante manter a palavra o mais fiel possível a original, por isso devem ser alteradas o mínimo número de letras possível.

Por exemplo, a palavra "HoUse" deve ser substituída por "house" e a palavra "LEgAL" por "LEGAL". Se uma palavra contém um número igual de letras maiúsculas e minúsculas, você deve substituir todas as letras maiúsculas por minúsculas, como por exemplo a palavra "PaGoDe" deve ser substituída por "pagode".

Sua tarefa é ler uma palavra da entrada e realizar a substituição necessária.



Entrada

A entrada consiste de uma string s
, associada à palavra em questão. A string s
 possui apenas letras de "a" a "z" maiúsculas e minúsculas com comprimento entre 1
 e 100
.



Saída

Imprima a string s
 corrigida. Se s
 possui estritamente mais letras maiúsculas, faça a palavra inteira ter letras maiúsculas, e vice-versa.
 '''
def corrigir_palavra(s):
    if sum(1 for c in s if c.isupper()) > len(s) // 2:
        print(s.upper())
    else:
        print(s.lower())

s = input()
corrigir_palavra(s)
