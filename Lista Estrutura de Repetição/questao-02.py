'''
Jordan quer resolver um problema muito interessante. Dadas as informações sobre o tamanho da população e a taxa de crescimento de duas cidades quaisquer (A e B), ele gostaria de saber quando a cidade menor (sempre é a cidade A) irá alcançar a cidade B em população (se é que vai alcançar). Sua tarefa é construir um programa que faça esses cálculos, porém, em alguns casos o tempo pode ser muito grande, e Jordan não se interessa em saber exatamente o tempo para estes casos.



Entrada
A entrada contém 4 valores: dois inteiros  (100≤PA,PB≤1000000
) indicando respectivamente a população de A e B, e dois valores  (0.0≤T1,T2≤100.0
), indicando respectivamente, em percentual, o crescimento populacional de A e B.



Saída
A saída deverá ser "Mais de um milenio." se a quantidade de anos for superior a 1000, "Vai alcancar em X ano(s).", onde X representa a quantiade de anos para a população de A alcançar o tamanho da população de B, ou "A nunca alcancara B.", se a população nunca for alcançar a população de B.



Notas
A população é sempre um valor inteiro, portanto, um crescimento de 2.5% sobre uma população de 100 pessoas resultará em 102 pessoas, e não 102.5 pessoas, enquanto um crescimento de 2.5% sobre uma população de 1000 pessoas resultará em 1025. Para coletar a parte inteira de um número em ponto flutuante, considere a utilização da função int.
'''
def calcular_anos_ate_alcancar(pa, pb, t1, t2):
    anos = 0
    while pa < pb:
        anos += 1
        pa += int(pa * (t1 / 100))
        pb += int(pb * (t2 / 100))
        
        # Se já passou de 1000 anos, retorna imediatamente
        if anos > 1000:
            return "Mais de um milenio."

    return f"Vai alcancar em {anos} ano(s)."

# Entrada de dados
pa, pb, t1, t2 = map(float, input().split())
pa, pb = int(pa), int(pb)

# Condição de não alcançar
if t1 <= t2 and pa < pb:
    print("A nunca alcancara B.")
else:
    resultado = calcular_anos_ate_alcancar(pa, pb, t1, t2)
    print(resultado)


