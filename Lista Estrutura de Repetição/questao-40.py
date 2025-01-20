'''
Dêivis está montando um site de E-Commerce, mas antes de começar, ele percebeu que precisaria de um validador de senhas para conseguir validar as senhas dos usuários. Como Dêivis não é um profissional em segurança, ele pediu que você faça o validador de senhas!

Para uma senha ser segura, ela precisa dos seguintes requisitos:

Ela deve conter, no mínimo, uma letra maiúscula, uma letra minúscula e um número;
Ela não pode ter nenhum caractere de pontuação, acentuação ou espaço;
Ela pode ter de 6 a 32 caracteres.

Entrada
A entrada contém uma linha com uma string, que é a senha que precisa ser verificada.


Saída
A saída contém uma linha, que pode ser “Senha valida.”, caso a senha tenha cada item dos requisitos solicitados anteriormente, ou “Senha invalida.”, se um ou mais requisitos não forem atendidos.
'''
# Leitura da entrada
senha = input()

# Condição 1: verificar se o comprimento da senha está entre 6 e 32 caracteres
if len(senha) < 6 or len(senha) > 32:
    print("Senha invalida.")
else:
    # Condição 2: verificar se contém pelo menos uma letra maiúscula, uma minúscula e um número
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)

    # Condição 3: verificar se não há caracteres de pontuação, acentuação ou espaços
    tem_caracter_invalido = any(not c.isalnum() for c in senha)

    # Verifica se todas as condições são atendidas
    if tem_maiuscula and tem_minuscula and tem_numero and not tem_caracter_invalido:
        print("Senha valida.")
    else:
        print("Senha invalida.")
