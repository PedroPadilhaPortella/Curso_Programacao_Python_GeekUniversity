numero1 = int(input("Numero 1:"))
n = 2
maior = numero1
menor = numero1
while(n <= 10):
    numero = int(input(f"Numero {n}: "))
    if(numero > maior):
        maior = numero
    if(numero < menor):
        menor = numero
    n += 1
print("Maior Valor: {}\nMenor Valor: {}".format(maior, menor))