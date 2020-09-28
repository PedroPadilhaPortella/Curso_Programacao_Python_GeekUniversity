from math import pow, sqrt
n = 1
while(n > 0):
    try:
        n = int(input("Valor Inteiro Positivo: "))
        print(f"{n} -- {pow(n, 2)} -- {pow(n, 3)} -- {sqrt(n)}")
    except:
        print("Valor na Range inválida")