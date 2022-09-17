'''
    Novas Funções Matemáticas e Estatísticas

    math.prod() -> calcula o produto dos elementos de um iterável (como listas e sets);
    math.isqrt() -> calcula a parte inteira da raiz quadrada de um numero;
    math.dist() -> calcula a distância euclidiana entre dois pontos;
    math.hypot() -> calcula a hipotenusa ou norma euclidiana;

    statistics.mean() -> calcula a média aritmética de números inteiros;
    statistics.fmean() -> calcula a média aritmética de números reais;
    statistics.geometric_mean() -> calcula a média geométrica de números reais;
    statistics.multimode() -> retorna um iterável com o elemento mais frequênte num conjunto de iteráveis;
'''

import math
import statistics

# prod
numeros = [2, 4, 6, 8]
print(math.prod(numeros))

# isqrt
print(math.isqrt(19))

# dist entre pontos 2D
ponto1 = [4, 4]
ponto2 = [4, 5]
print(math.dist(ponto1, ponto2))

# dist entre pontos 3D
ponto3 = [4, 4, 4]
ponto4 = [4, 5, 6]
print(math.dist(ponto3, ponto4))

# hypot
print(math.hypot(3, 4))
print(math.hypot(*ponto1))

#  ESTATISTICA

# fmean
print(statistics.mean([1, 2, 3, 4, 5]))
print(statistics.fmean([1, 2, 3, 4, 5]))

# geometric_mean
print(statistics.geometric_mean([1, 2, 3, 4, 5]))

# multimode
print(statistics.multimode([1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 6]))