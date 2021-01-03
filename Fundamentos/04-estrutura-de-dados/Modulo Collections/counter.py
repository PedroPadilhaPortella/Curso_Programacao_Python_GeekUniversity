'''
Module Collections -> High Performance Container Datetypes

Counter (Contador) => recebe um iterável e criar um objeto do tipo Collection Counter, que é semelhante a um dicionário, contendo como chave o elemento passado por parâmetro e como valor a quantidade de elementos encontrados, como um contador.
'''

from collections import Counter

lista = [1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7, 7, 11, 11, 11, 11, 11, 45, 24, 34, 0, 0]
gols = ['Pedro', 'João', 'João', 'Gabriel', 'Vinicius', 'Gabriel', 'Gabriel', 'Pedro', 'João', 'João', 'João']

c = Counter(lista)
estatisticas = Counter(gols)
print(type(c))

print(c)
print("\nESTATISTICAS DOS JOGADORES: ")
print(estatisticas)

print(Counter("Pedro Henrique Padilha Portella da Cruz"))

travalingua = "disseram que na minha rua tem paralelepípedo feito de paralelogramos seis paralelogramos tem um paralelepípedo mil paralelepípedos tem uma paralelepipedovia uma paralelepipedovia tem mil paralelogramos então uma paralelepipedovia é uma paralelogramolândia"

palavras = travalingua.split()

res = Counter(palavras)

print(res)
print(res.most_common(5))

help(Counter)