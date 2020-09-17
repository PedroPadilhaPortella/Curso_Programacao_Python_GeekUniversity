numero = int(input("Quantos Impares Naturais? "))
i = 0
while(numero > 0):
    i += 1
    if(i % 2 != 0):
        print(i)
        numero -= 1