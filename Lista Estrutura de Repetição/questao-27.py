'''
Ajude a escreva um programa para jogar o Jogo da Forca. 

O jogo da forca é um jogo em que o jogador tem que acertar qual é a palavra proposta, tendo como dica o número de letras e o tema ligado à palavra. A cada letra errada, é desenhado uma parte do corpo do enforcado. O jogo termina ou com o acerto da palavra ou com o término do preenchimento das partes corpóreas do enforcado.



Entrada 
Ler a palavra secreta e os caracteres para preencher as lacunas.



Saída 
Imprimir as  lacunas preenchidas da palavra secreta e o desenho da forca com o estado atual do jogo. 

Observação 
As lacunas de uma palavra devem ser representadas por meio do caractere _  (traço baixo) seguido de espaço. Na medida que a palavra secreta é descoberta, as lacunas devem ser preenchidas. Segue um exemplo para a palavra secreta arara:

_ _ _ _ _ 
a _ a _ a


O desenho inicial da forca vazia deverá ser preenchido com o símbolo hífen (-), soma (+) e igual (=)  e impressa desta forma:



 +---+
 |   |
     |
     |
     |
     |
========
Durante a partida, o desenho da forca deverá ser preenchido com os caracteres O (o maiúsculo), / (barra) e \ (barra inversa) até completar o seguinte desenho:


 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========
'''
def exibir_forca(erros):
    """Função para exibir o estado atual da forca, conforme o número de erros."""
    estados = [
        """
 +---+
 |   |
     |
     |
     |
     |
========
""",
        """
 +---+
 |   |
 O   |
     |
     |
     |
========
""",
        """
 +---+
 |   |
 O   |
 |   |
     |
     |
========
""",
        """
 +---+
 |   |
 O   |
/|   |
     |
     |
========
""",
        """
 +---+
 |   |
 O   |
/|\  |
     |
     |
========
""",
        """
 +---+
 |   |
 O   |
/|\  |
/    |
     |
========
""",
        """
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========
"""
    ]
    print(estados[erros])

def jogar_forca():
    palavra_secreta = input("Digite a palavra secreta: ").lower().strip()

    # Validação para garantir que a palavra secreta tenha apenas letras e não esteja vazia
    while not palavra_secreta.isalpha() or len(palavra_secreta) == 0:
        print("Por favor, digite uma palavra válida (somente letras).")
        palavra_secreta = input("Digite a palavra secreta: ").lower().strip()

    letras_descobertas = ['_'] * len(palavra_secreta)
    letras_erradas = []
    erros = 0

    while erros < 6:
        exibir_forca(erros)
        print(' '.join(letras_descobertas))
        letra = input("Digite uma letra: ").lower().strip()

        # Valida a entrada da letra
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite uma única letra válida.")
            continue

        # Verifica se a letra foi tentada antes
        if letra in letras_descobertas or letra in letras_erradas:
            print(f"Você já tentou a letra {letra}. Tente outra.")
            continue

        # Verifica se a letra está na palavra secreta
        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_descobertas[i] = letra
        else:
            letras_erradas.append(letra)
            erros += 1

        # Verifica se a palavra foi completamente descoberta
        if ''.join(letras_descobertas) == palavra_secreta:
            exibir_forca(erros)
            print(' '.join(letras_descobertas))
            print(f'Sim! A palavra secreta eh "{palavra_secreta}"')
            break

    if erros == 6:
        exibir_forca(erros)
        print(' '.join(letras_descobertas))
        print("Voce teve muitas oportunidades e perdeu!")

# Inicia o jogo
jogar_forca()
