"""
Nem mesmo a intervenção do Banco Central nesta terça evitou que a moeda americana registrasse sua quarta alta seguida na bolsa de valores.

Sua casa de câmbio vende dólares em lotes, por uma módica taxa adicional de 2,5% por lote (devido a contratos de ativos futuros). Implemente um programa para computar o valor final a ser cobrado em uma venda.

Entrada
A entrada consiste em uma linha com um valor real positivo 0≤n
, representando a atual cotação do dólar. A linha seguinte apresenta um valor inteiro positivo 0≤l
 indicando o tamanho do lote (quantos dólares serão comprados). A última linha apresenta um valor inteiro positivo indicando a quantidade de lotes 0≤q
 a serem vendidos. 

Saída
Apresente, para cada lote, uma linha contendo a mensagem indicando o número do lote e seu custo para o cliente, com duas casas decimais, conforme os exemplos.
"""

# Entrada dos valores
cotacao = float(input())
tamanho_lote = int(input())
quantidade_lotes = int(input())

# Calculando o valor total para cada lote com a taxa adicional
valor_por_lote = tamanho_lote * cotacao * 1.025

# Iterando e exibindo os resultados para cada lote
for i in range(1, quantidade_lotes + 1):
    print(f"Lote: {i} - Total da venda: R$ {valor_por_lote:.2f}")
