'''
Codifique um programa que leia um número inteiro e crie um novo número em ordem reversa a do fornecido. Por exemplo, se a entrada for 7395 a saída será 5937. Em caso de valores negativos, deve-se preservar o sinal.



Entrada
Um inteiro n
 tal que −108≤n≤108
.



Saída
Uma saída contendo o número n
 revertido.
 '''
# Leitura do número
n = int(input())

# Verificação se o número é negativo
if n < 0:
    # Inverte os dígitos, ignora o sinal
    reversed_n = int('-' + str(abs(n))[::-1])
else:
    # Inverte os dígitos normalmente
    reversed_n = int(str(n)[::-1])

# Exibe o número invertido
print(reversed_n)
