'''
Escreva um programa que leia um número n
 e percorra todos os números de 1 a n
 os exibindo segundo as seguintes regras: se for múltiplo de 3, deve mostrar "Fizz"; se for múltiplo de 5, deve mostrar "Buzz"; se for múltiplo de 3 e 5 deve mostrar "Fizz Buzz"; senão, mostrar o próprio número.



Entrada
A entrada consiste de uma linha contendo o valor de 1≤n≤100
.



Saída
A saída consiste de n
 linhas, cada uma contendo um número ou palavra(s) conforme a descrição.



Observação
No primeiro exemplo, nenhum número é múltiplo. No segundo caso, há dois múltiplos de 3 e um múltiplo de 5. No último exemplo, n
 é grande o suficiente para, eventualmente, todas as condições de multiplicidade serem atendidas.
 '''
# Lê o valor de n
n = int(input())

# Percorre todos os números de 1 a n
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
