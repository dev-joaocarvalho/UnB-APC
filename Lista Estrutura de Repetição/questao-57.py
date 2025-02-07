'''
A pandemia do novo Coronavírus fez com que a comunidade científica concentrasse esforços no desenvolvimento de soluções para minimizar todos os contratempos que a Covid-19 pudesse causar na sociedade. O laboratório Mahindra realizou grandes investimos para realizar pesquisas relacionadas no desenvolvimento de vacinas, medicamentos, equipamentos de proteção individual e as propriedades do vírus Sars-Cov-2.

O grupo de virologia, coordenado pelo renomado Dr. Pahal Sorabjee, está empenhado em compreender a estrutura do novo Coronavírus. Tentando entender suas origens e similaridades com outros vírus, a sequência de RNA do Sars-Cov-2 tem sido objeto de estudos, sendo comparada com sequências de RNA de outros tipos de vírus, como o Influenza, H1N1, HIV, entre outros. A primeira abordagem adotada pelos pesquisadores começou pela comparação das estruturas primárias entre duas sequências de RNA. Assumindo que uma sequência de RNA é caracterizada pelas bases nitrogenadas Adenina (A), Citosina (C), Guanina (G) e Uracila (U), os pesquisadores selecionam duas sequências distintas de RNA X=x1x2...xN
 e Y=y1y2...yN
, em que xi,yi∈{A,C,G,U}
 e N
 é a quantidade máxima de proteínas em cada uma. Em seguida, eles calculam a distância entre as sequências X
 e Y
 pela comparação posição a posição das bases e contabilização da quantidade de posições nas quais elas diferem entre si.

No entanto, a grande quantidade de amostras de vírus torna esse procedimento bastante complicado e, por isso, o Doutor Sorabjee o contactou para colaborar com a equipe. Sua tarefa consiste em elaborar um programa que receba duas sequências de RNA X
 e Y
 e calcular a distância entre elas conforme o procedimento inicial adotado pela equipe de pesquisadores.



Entrada
A entrada consiste em duas linhas, em que cada uma descreve uma sequência de RNA como uma string de comprimento N
 (1≤N≤10^5)
. A primeira linha apresenta a sequência X=x1x2...xN
, enquanto que a segunda linha descreve a sequência Y=y1y2...yN
. Assim, cada caractere de uma sequência está associado a uma das possíveis bases nitrogenadas, sendo garantido que cada string contenha apenas os caracteres 'A', 'C', 'G' e 'U'.



Saída
Imprima um número inteiro que determina a distância entre as duas sequências de RNA X
 e Y
.



Notas
No primeiro exemplo de teste, as bases nitrogenadas das duas sequências que são distintas estão destacadas em negrito: GUCA e AGCA. Portanto, a resposta é 2
.
'''

def distancia_rna(X, Y):
    distancia = sum(1 for x, y in zip(X, Y) if x != y)
    print(distancia)

X = input()
Y = input()
distancia_rna(X, Y)
