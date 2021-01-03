def calcularMultiplos(n, i, j):
    arr = []
    iterator = 0
    while(n > 0):
        if(iterator % i == 0 or iterator % j == 0):
            arr.append(iterator)
            n -= 1
        iterator += 1
    return arr




i = int(input("insira um valor: "))
j = int(input("insira outro valor: "))
n = int(input(f"Quantos multiplos de {i} e {j}? "))
array = calcularMultiplos(n, i, j)
print("Os primeiros {} valores multiplos de {} e {} foram: {}".format(n, i, j, array))