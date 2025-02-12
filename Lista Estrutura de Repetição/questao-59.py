'''
Calcule o tamanho de uma string, SEM UTILIZAR O MÉTODO "len()" DISPONÍVEL NO PYTHON.



Entrada

A entrada contém uma linha, que consiste de uma string.



Saída
A saída possui uma linha, que é o tamanho da string.



Notas

Se o método "len()" for utilizado, a questão dará as repostas como erradas.

'''
# Lê a string de entrada
s = input().strip()

# Inicializa um contador
count = 0

# Itera sobre cada caractere da string e incrementa o contador
for char in s:
    count += 1

# Imprime o tamanho da string
print(count)
