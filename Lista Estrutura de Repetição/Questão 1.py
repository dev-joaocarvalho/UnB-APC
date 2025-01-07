# Entrada dos valores
cotacao = float(input())
tamanho_lote = int(input())
quantidade_lotes = int(input())

# Calculando o valor total para cada lote com a taxa adicional
valor_por_lote = tamanho_lote * cotacao * 1.025

# Iterando e exibindo os resultados para cada lote
for i in range(1, quantidade_lotes + 1):
    print(f"Lote: {i} - Total da venda: R$ {valor_por_lote:.2f}")
