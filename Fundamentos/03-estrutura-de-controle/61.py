def calcular():
    maior = 0
    n = 0
    my = 0
    mx = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            n = x * y
            n = str(n)
            if(n == n[::-1]):
                n = int(n)
                print(n)
                if(n > maior):
                    maior = n
                    my = y
                    mx = x
    return [maior, mx, my]

[maior, mx, my] = calcular()
print("O maior palindromo formado pela multiplicação de dois numeros de 3 algarismos é: {}\nQue é o produto entre {} e {}".format(maior, mx, my))