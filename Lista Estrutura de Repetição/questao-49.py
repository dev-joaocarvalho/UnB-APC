'''
Semana passada a tumba do lendário feiticeiro Mellin foi aberta para que cientistas ao redor do mundo decodificassem seu DNA.

Essa tarefa está quase acabando, só o que falta é recuperar alguns nucleotídeos de uma cadeia s
. Cada nucleotídeo é codificado como uma letra maiúscula do alfabeto português: "A", "C", "G" ou "T". Nucleotídeos não reconhecidos são codificados com um ponto de interrogação "?". Assim, s
 é uma cadeia com caracteres "A", "C", "G", "T" e "?".

Sabe-se que em uma cadeia, cada nucleotídeo deve aparecer um número igual de vezes.

Sua tarefa é decodificar o genoma e substituir cada nucleotídeo não-reconhecido por um dos quatro tipos reconhecidos de modo que o número de cada um dos quatro tipos seja igual.



Entrada

A primeira linha contém um inteiro n
 (4≤n≤255
), representando o comprimento do genoma.

A segunda linha contém a string s
 de comprimento n
 - o genoma codificado, que é caracterizada por uma cadeia com caracteres "A", "C", "G", "T" e "?".



Saída

Se for possível decodificar o genoma, imprima "Segredos desvendados". Se não for possível, imprima "Feiticeiro misterioso" .
'''
def decodificar_genoma(n, s):
    count_a = s.count('A')
    count_c = s.count('C')
    count_g = s.count('G')
    count_t = s.count('T')
    count_question = s.count('?')
    
    # Calcular o número de nucleotídeos de cada tipo para o genoma ser válido
    target_count = n // 4
    
    if n % 4 != 0:
        print("Feiticeiro misterioso")
        return
    
    # Verificar se é possível ajustar os nucleotídeos não reconhecidos
    needed_a = target_count - count_a
    needed_c = target_count - count_c
    needed_g = target_count - count_g
    needed_t = target_count - count_t
    
    total_needed = needed_a + needed_c + needed_g + needed_t
    
    if total_needed == count_question and all(x >= 0 for x in [needed_a, needed_c, needed_g, needed_t]):
        print("Segredos desvendados")
    else:
        print("Feiticeiro misterioso")

n = int(input())
s = input()
decodificar_genoma(n, s)
