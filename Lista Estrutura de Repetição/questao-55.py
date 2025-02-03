'''
Seu Donato é professor de português em uma escola de educação básica e está corrigindo as redações dos alunos, que foram entregues ao docente por meio de um software educacional. Ao corrigir as redações, Seu Donato percebeu que a maioria dos alunos estava errando a escrita de palavras para a seguinte regra ortográfica da língua portuguesa:


"Deve-se empregar a consoante m antes das consoantes p e b para a criação dos sons am, em, im, om e um."

As palavras "pombo", "bombeiro" e "tampa" são exemplos corretos que respeitam a regra ortográfica acima. No entanto, Seu Donato percebeu que os alunos estavam escrevendo incorretamente essas palavras como "ponbo", "bonbeiro" e "tanpa". Tais erros se repetiram para diversas outras palavras da língua portugesa conforme explicitado na regra específica.

Seu Donato quer sua ajuda. Ele gostaria que você ajustasse o software educacional para detectar esses erros nas redações dos alunos. Por isso, dada uma sentença de uma redação de um aluno qualquer, imprima a sentença com as correções necessárias quando alguma consoante n aparecer antes das letras b e p.



Entrada
A entrada consiste de uma única linha contendo uma string s
 associada a uma sentença da redação de algum aluno. A string s
 pode conter, no máximo, 1000
 caracteres e contém todos os caracteres entre 'a' e 'z' (é garantido que todas esses caracteres são minúsculos), como também caracteres de espaço em branco.



Saída
Imprima a sentença lida na entrada da maneira correta conforme a regra ortográfica da língua portuguesa descrita no enunciado.
'''
def corrigir_ortografia(sentenca):
    corrigida = sentenca.replace('nb', 'mb').replace('np', 'mp')
    print(corrigida)

sentenca = input()
corrigir_ortografia(sentenca)
