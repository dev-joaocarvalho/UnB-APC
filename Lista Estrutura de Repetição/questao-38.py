'''
Thiago e Geraldo estão jogando uma disputada partida batalha naval 1D online. O jogo ocorre em um mapa unidimensional, que representa o oceano, sendo dividido em pequenas regiões. Cada região pode indicar apenas água ou a presença de um navio. Como alguns navios podem ser grandes, eles podem ocupar duas ou mais regiões contíguas. Um exemplo de representação visual de um mapa 1D nessa batalha naval é fornecida abaixo:

                                                                                                                               ..o....oooo...oo..o.

em que '.' indica uma região que contém apenas água, enquanto que 'o' está associada a um navio, ou apenas parte dele. Nesse mapa, nota-se a presença de 4
 navios.

Você conseguiu o mapa 1D do Geraldo, contendo o posicionamento de todos os seus navios. Nessa batalha naval, um disparo que atinge um navio ou parte dele, é suficiente para afundá-lo. Escreva um programa que determine a quantidade mínima de disparos certeiros (que atingem um navio ou parte dele) que Thiago deve efetuar para afundar todos os navios colocados por Geraldo no seu mapa 1D.



Entrada

A entrada consiste de uma string s=s1s2…sn
 (1≤n≤5×10^2)
 representando o mapa unidimensional do Geraldo, em que si=
 '.' indica água e si=
 'o' indica que nessa região existe um navio, ou parte dele. É garantido que Geraldo tenha posicionado pelo menos um navio no seu mapa.


Saída

Imprima um único número inteiro que indica a quantidade mínima de disparos certeiros que Thiago pode disparar para afundar todos os navios de Geraldo.
'''
  # Leitura do mapa do jogo
mapa = input().strip()

# Inicialização do contador de disparos
disparos = 0

# Vamos percorrer a string e contar as sequências de 'o'
for i in range(1, len(mapa)):
    if mapa[i] == 'o' and mapa[i-1] == '.':
        disparos += 1

# Caso o mapa comece com 'o', devemos contar também
if mapa[0] == 'o':
    disparos += 1

# Imprimir o número de disparos necessários
print(disparos)
