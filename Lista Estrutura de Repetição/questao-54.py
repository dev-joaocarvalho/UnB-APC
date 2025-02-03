'''
Deivis decidiu parar de pedir ajuda e começou a fazer aulas de programação. Sua primeira lição é escrever um programa simples: dada uma palavra com letras maiúsculas e minúsculas, ele:

Deleta todas as vogais;
Coloca o caractere "." antes de cada consoante;
Substitui todas as consoantes maiúsculas por minúsculas.
O curso é americano então as vogais são as letras "A", "O", "Y", "E", "U" e "I". A entrada do programa é exatamente uma palavra e o programa deve imprimir exatamente uma string processada de acordo com as regras.

Deivis está vendo que programar não é para ele e está precisando novamente da sua ajuda.



Entrada

A entrada consiste de uma palavra com apenas letras maiúsculas e minúsculas com tamanho entre 1 e 100, inclusive.



Saída

Imprima o resultado da palavra após ser processada. É garantido que o resultado final nunca será vazio.
'''
def processar_palavra(palavra):
    vogais = set("aoyeuiAOYEUI")
    resultado = ''.join(f".{c.lower()}" for c in palavra if c not in vogais)
    print(resultado)

palavra = input()
processar_palavra(palavra)
