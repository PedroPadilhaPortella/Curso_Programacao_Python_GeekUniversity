def primos_ate(numero):
    primos = set()
    for i in range(0, numero):
        for j in range(1, i):
            if(i % j == 0):
                primos.add(i)
    return primos

numero = int(input("Defina um limite pra encontrar os primos: "))
print(f"Os primos até {numero} são {primos_ate(numero)}")