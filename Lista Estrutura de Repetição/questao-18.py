'''
Para automatizar o cálculo da nota dos alunos na disciplina de Algoritmos e Programação de Computadores, o professor da disciplina solicitou a sua ajuda para criar um programa que calcule a média das três avaliações somativas de cada um dos alunos e o informe se o aluno foi aprovado ou não. Nesta disciplina, o aluno é aprovado se sua a nota é maior ou igual a 7.0.

Entrada
A primeira linha contém um inteiro N
 (1≤N≤50
 ) que representa a quantidade de alunos da turma. Cada uma das N
 linhas seguintes contém 3 valores do tipo double representando cada um as respectivas notas as1
, as2
 e as3
 de cada uma das avaliações somativas do aluno (0.0≤asi≤10
).



Saída
A saída deve conter uma linha para cada aluno com a frase "O ALUNO X FOI APROVADO" se o aluno foi aprovado na média final ou "O ALUNO X FOI REPROVADO" se o aluno foi reprovado na média final, onde X representa o índice do aluno, conforme apresentado nos exemplos.
'''
# Lê o número de alunos
N = int(input())

# Processa cada aluno
for i in range(N):
    # Lê as três notas do aluno
    as1, as2, as3 = map(float, input().split())
    
    # Calcula a média
    media = (as1 + as2 + as3) / 3
    
    # Verifica se o aluno foi aprovado ou reprovado
    if media >= 7.0:
        print(f"O ALUNO {i} FOI APROVADO")
    else:
        print(f"O ALUNO {i} FOI REPROVADO")
