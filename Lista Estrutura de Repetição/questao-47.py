'''
Construa um programa para verificar, à partir de dois valores A e B, se B corresponde aos últimos dígitos (os menos significativos, mais à direita) de A.



Entrada
A entrada consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 100 dígitos.



Saída
Imprima "ta dentro!!!" se B corresponde aos últimos dígitos de A, e "ta fora..." caso contrário.
'''
def verificar_ultimos_digitos(a, b):
    if a.endswith(b):
        print("ta dentro!!!")
    else:
        print("ta fora...")

a, b = input().split()
verificar_ultimos_digitos(a, b)
