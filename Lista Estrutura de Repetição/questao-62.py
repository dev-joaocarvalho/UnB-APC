'''
Deivis começou a trabalhar de DJ nas maiores festas da UnB e ele gosta muito de tocar dubstep, apesar de já ser 2020. Recentemente, ele decidiu pegar algumas músicas antigas e fazer remixes dubstep delas.

Vamos assumir que uma música consiste de uma determinada quantidade de palavras. Para fazer o remix dubstep desta música, Deivis pode incluir algumas palavras "WUB" antes da primeira palavra da música (o número pode ser 0), depois da última palavra (o número pode ser 0) e entre palavras (existe pelo menos um WUB entre cada par de palavras vizinhas), e aí ele junta todas as palavras, incluindo os "WUB"s em uma só palavra e toca a música na festa.

Por exemplo, uma música com as palavras "I AM X" podem ser remixadas para "WUBWUBIWUBAMWUBWUBX", mas não para "WUBWUBIAMWUBX".

Recentemente, Pepper ouviu o último remix dubstep do Deivis, mas como ele já passou dessa fase, ele decidiu descobrir qual era a música inicial que o Deivis remixou. Ajude ele!



Entrada

A primeira linha de entrada contém uma palavra s
 - uma palavra com apenas letras de "a" a "z" maiúsculas e minúsculas com comprimento entre 1
 e 200
. É garantido que antes de Deivis ter remixado a música, nenhuma palavra continha "WUB" nela. Deivis também não trocou a ordem das palavras. Também é garantido que a música original tinha pelo menos uma palava.



Saída

Imprima as palavras da música original que Deivis remixou. Separe as paalvras com um espaço.
'''
def remover_wub(s):
    # Dividimos a string usando 'WUB' e filtramos as partes não vazias
    palavras = s.split("WUB")
    # Filtra palavras vazias
    palavras = [palavra for palavra in palavras if palavra]
    # Junta as palavras com um espaço
    return " ".join(palavras)

# Leitura da entrada
entrada = input().strip()

# Chama a função para remover os 'WUB' e imprime a música original
print(remover_wub(entrada))
