def divisor(num):
    divisores = []
    for i in range(1, num):
        if(num % i == 0):
            divisores.append(i)
    return divisores


num = int(input("Insira um numero positivo: "))
divisores = divisor(num)
print("O divisores de {} são : {}".format(num, divisores))
if(len(divisores) == 1):
    print("Numero Primo!!")