'''
Desenvolva um programa que leia uma string e imprima cinco versões dessa mesma string, uma por linha, sendo que em cada versão, todas as vogais minúsculas devem ser substituídas por uma vogal x
, definida abaixo:

Na primeira versão dessa string, x
 = 'a';
Na segunda versão dessa string, x
 = 'e';
Na terceira versão dessa string, x
 = 'i'; 
Na quarta versão dessa string, x
 ='o' ;
Na segunda versão dessa string, x
 = 'u'.


Entrada 

A entrada consiste de uma única string, contendo até 100
 caracteres. A string contém apenas letras minúsculas do alfabeto.



Saída

A saída contém cinco linhas, cada uma composta por uma versão da string fornecida na entrada, isto é, cada uma delas apresenta apenas um tipo de vogal.

'''

def substituir_vogais(string):
    vogais = ['a', 'e', 'i', 'o', 'u']
    for vogal in vogais:
        resultado = ''.join(vogal if c in 'aeiou' else c for c in string)
        print(resultado)

entrada = input()
substituir_vogais(entrada)
