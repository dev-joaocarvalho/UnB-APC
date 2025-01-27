'''
De vez em quando palavras como "localization" ou "internationalization" são tão longas que escrevê-las muitas vezes no mesmo texto fica cansativo.

Vamos considerar uma palavra "muito longa" se seu número de caracteres for estritamente maior que 10. Todas as palavras muito longas devem ser substituídas por uma abreviação especial.

A abreviação funciona assim: nós escrevemos a primeira e a última letra de uma palavra, e entre elas nós escrevemos o número de letras entre a primeira e última letra. O número está no sistema decimal e não contém zeros à esquerda.

Deste modo, "localization" é abreviado para "l10n" e "internationalization" é abreviado para "i18n".

Você tem a tarefa de automatizar o processo de mudar as palavras pelas suas abreviações. Todas as palavras muito longas devem ser abreviadas e palavras não muito longas não devem ser modificadas.



Entrada

A primeira linha de entrada contém um inteiro n(1≤n≤100)
. Cada uma das próximas n
 linhas contém uma palavra. Todas as palavras contém apenas letras de "a" a "z", todas minúsculas e possuem comprimento de 1
 a 10^4
 caracteres.



Saída

Imprima n
 linhas. A i-ésima linha deve conter o resultado de substituir (ou não) a i-ésima palavra da entrada.
 '''
def abreviar_palavra(palavra):
    if len(palavra) > 10:
        return f"{palavra[0]}{len(palavra) - 2}{palavra[-1]}"
    return palavra

n = int(input())
for _ in range(n):
    palavra = input()
    print(abreviar_palavra(palavra))
