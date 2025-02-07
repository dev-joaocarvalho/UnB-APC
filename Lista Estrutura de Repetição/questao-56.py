'''
Dêivis está montando um site de E-Commerce, mas antes de começar, ele percebeu que precisaria de um validador de senhas para conseguir validar as senhas dos usuários. Como Dêivis não é um profissional em segurança, ele pediu que você faça o validador de senhas!

Para uma senha ser segura, ela precisa dos seguintes requisitos:

Ela deve conter, no mínimo, uma letra maiúscula, uma letra minúscula e um número;
Ela não pode ter nenhum caractere de pontuação, acentuação ou espaço;
Ela pode ter entre 6 e 32 caracteres (inclusivo).
Input
A entrada contém uma linha com uma string, que é a senha que precisa ser verificada.

Output
A saída contém uma linha, que pode ser “Senha valida.” (sem aspas duplas), caso a senha tenha cada item dos requisitos solicitados anteriormente, ou “Senha invalida.” (sem aspas duplas), se um ou mais requisitos não forem atendidos.
'''

import re

def validar_senha(senha):
    if (6 <= len(senha) <= 32 and
        re.search(r'[a-z]', senha) and
        re.search(r'[A-Z]', senha) and
        re.search(r'[0-9]', senha) and
        re.match(r'^[A-Za-z0-9]+$', senha)):
        print("Senha valida.")
    else:
        print("Senha invalida.")

senha = input()
validar_senha(senha)
