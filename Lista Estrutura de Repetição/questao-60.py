'''
A tradução da linguagem Roq para a linguagem Ly não é fácil. As linguagens são muito similares: uma palavra roq-esa é diferenciada de uma palavra ly-esa com o mesmo significado de uma forma bem pequena: é escrita (e dita) ao contrário. Por exemplo, uma palavra roq-esa "code" corresponde à palavra ly-esa "edoc". Entretanto, é fácil cometer um erro durante a tradução. Deivis traduziu a palavra roq-esa s
 para a palavra ly-esa t
. Ajude-o a descobrir se a tradução está correta.



Entrada

A primeira linha contém a palavra s
 e a segunda linha contém a palavra t
. As palavras consistem de letras minúsculas de "a" a "z". A entrada não possui espaços desnecessários. As palavras não são vazias e seus comprimentos não excedem 100 caracteres.



Saída

Se a palavra t
 em ly-esa é equivalente a palavra s
 em roq-esa, imprima "Boa Deivis!" (sem as aspas duplas). Caso contrário, imprima "Poxa Deivis..." (sem as aspas duplas).
 '''
# Lê as duas palavras
s = input().strip()
t = input().strip()

# Verifica se t é o reverso de s
if s[::-1] == t:
    print("Boa Deivis!")
else:
    print("Poxa Deivis...")
