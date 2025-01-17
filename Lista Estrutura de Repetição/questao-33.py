'''
Implemente a função maior_norma que recebe dois vetores de dimensão 3, compara a norma L1 deles e diz qual é maior. A norma L1 pode ser definida como a soma dos valores absolutos de um vetor como dado na seguinte equação: norma-L1(x)=∑3i=1|xi|

Entrada
Não há entrada. Os parâmetros da função são duas listas de números.



Saída
A função deve imprimir “PRIMEIRO”, se o primeiro vetor tiver a maior norma, ou “SEGUNDO” caso contrário.
'''
def maior_norma(vetor1, vetor2):
    # Calcula a norma L1 dos dois vetores
    norma1 = sum(abs(x) for x in vetor1)
    norma2 = sum(abs(x) for x in vetor2)
    
    # Compara as normas e imprime o resultado
    if norma1 > norma2:
        print("PRIMEIRO")
    else:
        print("SEGUNDO")
