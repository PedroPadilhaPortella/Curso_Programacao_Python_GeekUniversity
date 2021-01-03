def sequencesI(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

def sequencesII(n):
    sum = 0
    last = (2 * n) - 1
    for i in range(1, last + 1):
        if(i % 2 == 0):
            sum -= i
        else:
            sum += i
    return sum

def sequencesIII(n):
    sum = 0
    last = (2 * n) - 1
    for i in range(1, last + 1):
        if(i % 2 != 0):
            sum += i
    return sum

n = int(input("Digite um Valor Inteiro: "))
sum1 = sequencesI(n)
sum2 = sequencesII(n)
sum3 = sequencesIII(n)
print(f"Sequencia 1 = {sum1}\nSequencia 2 = {sum2}\nSequencia 3 = {sum3}")