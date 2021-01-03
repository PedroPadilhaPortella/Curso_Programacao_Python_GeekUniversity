# Comprehentions
# [ expressao for item in list if condicional ]

dobro = []

# for i in range(1,  10):
#     dobro.append(i * 2)
# print(dobro)

dobro = [i * 2 for i in range(1, 10)]
print(dobro)


# for i in range(0,  20):
#     if(i % 2 == 0):
#         dobro.append(i)
# print(dobro)

dobro = [i for i in range(1, 20) if i % 2 == 0]
print(dobro)



# Generator

generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator)) # 0
print(next(generator)) # 4
print(next(generator)) # 16
print(next(generator)) # 36
print(next(generator)) # 64
# print(next(generator)) # Erro!

for numero in generator:
    print(numero)

 
# Dict Comprehention

dicio = {f"indice {i}" : i * 2 for i in range(10) if i % 2 == 0}
print(dicio)

for numero, dobro in dicio.items():
    print(f"{numero}: {dobro}")
