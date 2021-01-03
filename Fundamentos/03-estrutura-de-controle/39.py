def calcularTriangulo(base, altura):
    return base * altura / 2


base = 0
altura = 0
while(base <= 0 or altura <= 0):
    print("Calcular a area de um triangulo, somente medidas diferentes de 0")
    base = float(input("Base: "))
    altura = float(input("Altura: "))

a = calcularTriangulo(base, altura)
print("A area do triangulo de base = {} e altura = {} é {}".format(base, altura, a))