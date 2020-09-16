def parImpar(n):
    if(n % 2 == 0):
        return 'par'
    else:
        return 'impar'

n = int(input("Numero: "))
resultado = parImpar(n)
print("{} é {}".format(n, resultado))