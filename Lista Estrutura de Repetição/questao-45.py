'''
Por algum motivo acadêmico misterioso, o professor Mellin precisa urgentemente de um programa que acrescenta um espaço entre cada letra de uma frase, mas que não duplica espaços na frase, caso haja algum.



Entrada
A primeira linha apresenta uma frase com caracteres e espaços. 



Saída

Apresente, em uma linha, a frase acrescida de um espaço entre cada letra desta, sem duplicar espaços na frase, caso haja algum.
'''
def adicionar_espacos(frase):
    # Remover os espaços existentes e adicionar um espaço entre as letras
    frase_sem_espacos = frase.replace(" ", "")  # Remove espaços
    frase_com_espacos = " ".join(frase_sem_espacos)  # Adiciona espaço entre as letras
    print(frase_com_espacos)

frase = input()
adicionar_espacos(frase)
