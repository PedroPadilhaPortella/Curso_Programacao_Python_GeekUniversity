def verificarPrimo(n):
    i = 1
    primo = 0
    while(i <= n):
        if(n % i == 0 ):
            primo += 1
        i += 1
    if(primo > 2):
        return "não é primo"
    else:
        return "é primo"

n = int(input("Verifique se um numero é primo: "))
print("O numero {} {}".format(n, verificarPrimo(n)))