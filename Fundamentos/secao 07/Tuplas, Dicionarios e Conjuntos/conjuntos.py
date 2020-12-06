"""
Conjuntos

Os conjuntos são baseados na Teoria dos Conjuntos, 
--Eles são chamados de sets()
--Não possuem valores repetidos
--São estruturas não indexadas (seus elementos não podem ser acessados via indice).
--Possuem metodos como União e Interssecao, Subtracao, Distinct, etc.

São usados quando precisamos armazenar elementos mas não nos importamos com a ordenação, chave-valor e itens duplicados.
"""

conjunto = set({1, 2, 3, 4, 5, 1, 2, 3, 4, 5}) # conjunto
conjunto2 = set('pedro portella') # conjunto de string
lista = (1, 1, 1, 2, 0, 3, 4)
conjunto3 = set(lista) #conjunto convertido de uma lista
print(conjunto, conjunto2, conjunto3)

# conjuntos podem ser iterados e podem receber todos os tipos de dados
conj = {1, True, "Pedro", "Pedro", 5.6}
for i in conj:
    print(i)

# metodos de sets:
s = {1, 2, 3, 5, 6}
s.add(4)
s.add(4)
s.remove(1) # remove elementos, mas se não encontrar o valor, gera KeyError
s.discard(102) # remove elementos, e não gera keyError
print(s)

# Copiar um conjunto: DeepCopy e SwallowCopy:
novo = s.copy() #deepCopy
novo2 = s #shallowCopy
s.add(100)
print(novo, novo2)

#limpar um conjunto:
novo.clear()


# metodos matemáticos em Conjuntos:
python = {'pedro', 'gustavo', 'barbara', 'daniel', 'diego'}
java = {'pedro', 'rodrigo', 'barbara', 'carlos', 'henrique'}

print(f"Estudam python ou java: {python.union(java)}")
print(f"Estudam python ou java: {python | java}")
print(f"Estudam python e java: {python.intersection(java)}")
print(f"Estudam python e java: {python & java}")
print(f"Estudam apenas python: {python.difference(java)}")
print(f"Estudam apenas java: {java.difference(python)}")

# soma, maximo, minimo, tamanho => apenas com valores unicamente inteiros ou reais
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

