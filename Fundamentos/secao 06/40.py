def calcular():
    n = int(input("Numero: "))
    maior = n
    menor = n
    while(n > 0):
        n = int(input("Numero: "))
        if(n > maior and n >= 0):
            maior = n
        if(n < menor and n >= 0):
            menor = n
    print(f"\nMaior: {maior}")
    print(f"Menor: {menor}")


calcular()