'''
Nunão e Levinho amam futebol e estavam assistindo um clássico brasileiro, Corinthians x São Paulo. Estudiosos como são, eles escreviam as posições dos jogadores em uma peça de papel. Para simplificar a situação, as posições eram descritas como uma string contendo apenas zeros e uns. Um "0" corresponde a um jogador do Corinthians e um "1" corresponde a um jogador do São Paulo.

Se existem 7 jogadores de um time, um do lado do outro, então a situação é considerada favorável àquele time. Por exemplo, a situação "00100110111111101" é favorável ao São Paulo e a situação "11110111011101" não é favorável a ninguém.

Determine para qual time a situação é favorável.



Entrada

A primeira linha de entrada contém uma palavra s
 - uma palavra com apenas "0"s e "1s"  com comprimento entre 1
 e 100
. Existe pelo menos um jogador de cada time no campo.



Saída

Imprima "JOGO PESADO" se a situação for favorável para os dois times, "VAI TIMAO" se a situação for favorável apenas para o Corinthians, "VAMO TRICOLOR" se a situação for favorável apenas para o São Paulo e "BORA UM VIRTUAL NO CODEFORCES" se o jogo estiver entediante e a situação não for favorável para ninguém.
'''
def verificar_jogo(s):
    if "0000000" in s and "1111111" in s:
        print("JOGO PESADO")
    elif "0000000" in s:
        print("VAI TIMAO")
    elif "1111111" in s:
        print("VAMO TRICOLOR")
    else:
        print("BORA UM VIRTUAL NO CODEFORCES")

s = input()
verificar_jogo(s)
