'''
Venceslau está treinando uma equipe de futebol Pequi Futebol Clube (Pequi FC) e encontra dificuldades para escalar um time titular ideal. A equipe possui um elenco com n
 jogadores, em que o i-ésimo jogador possui nível técnico (habilidade) ai
. Quanto maior é o valor de ai
, mais habilidoso é o jogador em questão.

O Pequi FC está disputando a quinta divisão do Campeonato Goiano, em que cada equipe deve levar exatamente 11 jogadores a campo, definindo o time titular. Já para o banco de reservas, o clube pode levar, no máximo, 11 jogadores. Como Venceslau é um treinador com características ofensivas, ele sempre escala os melhores jogadores (os mais habilidosos) para o time titular e leva para o banco de reservas os jogadores mais habilidosos do elenco que não foram escalados como titulares. Infelizmente, alguns atletas do elenco podem não chegar a serem relacionados para o jogo.

Considerando que a soma da habilidades dos jogadores titulares e reservas sejam t
 e r
, respectivamente, escreva um programa que determine a maior diferença possível entre t
 e r
. Vale lembrar que, Venceslau sempre leva a maior quantidade possível de jogadores para os jogos, sendo sempre possível levar ao menos um time titular (11 jogadores) e um jogador reserva.



Entrada
A primeira linha da entrada contém um número inteiro n
 (12≤n≤102
), indicando a quantidade de jogadores no plantel do Pequi FC. A segunda linha contém n
 números inteiros separados por espaço, a1,a2,…,an
 (1≤ai≤100
), indicando a habilidade de cada jogador do plantel.



Saída
Imprima um número inteiro que expressa a maior diferença possível entre as somas das habilidades dos jogadores dos times titular e reserva.
'''
def maior_diferenca(n, habilidades):
    # Ordena a lista de habilidades de forma decrescente
    habilidades.sort(reverse=True)
    
    # Somas dos jogadores titulares e reservas
    t = sum(habilidades[:11])  # Primeiros 11 jogadores para o time titular
    r = sum(habilidades[11:22])  # Próximos 11 jogadores para o banco de reservas
    
    # Diferença entre as somas dos titulares e reservas
    return t - r

# Leitura da entrada
n = int(input())  # Número de jogadores no elenco
habilidades = list(map(int, input().split()))  # Lista de habilidades dos jogadores

# Chama a função para calcular a maior diferença e imprime o resultado
print(maior_diferenca(n, habilidades))

