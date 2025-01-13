'''
Um elefante incomoda muita gente, dois elefantes incomodam, incomodam muito mais... n+1
 elefantes incomodariam quanto mais?
Implemente um programa que recebe a quantidade de elefantes e escreva a letra da música.



Entrada
A entrada consiste de um número inteiro positivo 0<n≤500
 indicando a quantidade de elefantes.



Saída
A saída esperada é o refrão da música para a quantidade de elefantes dada, começando com 1 e incrementando até que se saiba dos  n+1
 elefantes. Apresente uma frase por linha.
 '''
def elefantes(n):
    if n < 1 or n > 500:
        print("Entrada inválida. O número deve ser entre 1 e 500.")
        return

    print("1 elefante incomoda muita gente...")
    for i in range(2, n + 1):
        print(f"{i} elefantes incomodam, " + "incomodam, " * (i-2) +"incomodam " + "muito mais...")
        print(f"{i} elefantes incomodam muita gente...")
    
    print(f"{n + 1} elefantes incomodam, " + "incomodam, " * (n-1) +"incomodam " + "muito mais...")

# Exemplo de uso:
n = int(input())
elefantes(n)
