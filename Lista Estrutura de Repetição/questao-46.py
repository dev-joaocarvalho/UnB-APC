'''
Depois de passar muito tempo na internet e perceber que as pessoas utilizam caixa alta para poder representar xingamentos e gritarias, lhe foi pedido que implementasse um programa que fosse exatamente na direção oposta a essas vulgaridades, que é transformar frases grotescas em frases polidas. Para este caso, uma frase polida é aquela em que o primeiro caracter (que sempre é uma letra) está em maiúsculo e o restante das letras está em minusculo.



Entrada
A primeira linha apresenta uma string de até 100 caracteres composta por caracteres legíveis e espaço. 



Saída

Apresente, em uma linha, a frase constituída pelo primeiro caractere que é uma letra em maiúsculo e todas as outras letras em minúsculo.
'''
def frase_politica(frase):
    print(frase.capitalize())

frase = input()
frase_politica(frase)
