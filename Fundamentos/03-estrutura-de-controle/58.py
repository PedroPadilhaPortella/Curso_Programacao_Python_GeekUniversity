def verificarPrimo(n):
    i = 1
    primo = 0
    while(i <= n):
        if(n % i == 0 ):
            primo += 1
        i += 1
    if(primo <= 2):
        return n
total = 0 
bottom = int(input("Calcular os Numeros Primos entre uma Range\nQual o limite inferior: "))
top = int(input("Qual o limite superior: "))
if(top < bottom):
    change = bottom
    bottom = top
    top = change

for n in range(bottom, top + 1):
    primo = verificarPrimo(n)
    if(primo):
        total += primo

print("A Soma dos numeros primos de {} a {} é {}".format(top, bottom, total))
