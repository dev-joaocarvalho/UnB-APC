'''
Um dia o rei Deivis viu uma criança passando fome na rua, ficou horrorizado e decidiu que nunca mais queria ver aquilo na vida dele. Por isso, ele decretou que todos os cidadãos do reino deveriam ter no mínimo 1000 de dinheiro. Mas Deivis só pode dar dinheiro, não tirar dos outros. Qual é a quantia mínima de dinheiro a ser gasta para que isso seja realizado?




Entrada
A primeira linha contém um inteiro 0≤n≤100
 representando o número de cidadãos no reino. As seguintes n
 linhas representam o dinheiro que cada cidadão tem.



Saída
Imprima um único inteiro que representa a quantia mínima de dinheiro a ser dada pelo Rei Deivis.
'''
# Lê o número de cidadãos
n = int(input())

# Variável para armazenar o total de dinheiro que o Rei precisa dar
total_dado = 0

# Para cada cidadão, lê o dinheiro e calcula a diferença se necessário
for _ in range(n):
    dinheiro = int(input())
    if dinheiro < 1000:
        total_dado += 1000 - dinheiro

# Imprime a quantia mínima a ser dada
print(total_dado)
