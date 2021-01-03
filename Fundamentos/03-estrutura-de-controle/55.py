def verificarPrimo(n):
    i = 1
    primo = 0
    while(i <= n):
        if(n % i == 0 ):
            primo += 1
        i += 1
    if(primo <= 2):
        return n
primos = []
numero = int(input("Digite um numero: "))
for n in range(1, numero + 1):
    primo = verificarPrimo(n)
    if(primo):
        primos.append(primo)

print("Os numero primos de 0 a {} são: \n{}".format(numero, primos))
