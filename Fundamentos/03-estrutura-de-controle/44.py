def fibonacci(number):
    fib = 0
    anterior = 0
    while(fib < number):
        print(fib)
        fib += anterior
        anterior = fib - anterior
        if(fib == 0):
            fib += 1
    else:
        print(fib)

number = int(input("Insira o valor aproximado até o qual a sequencia deve ir: "))
fibonacci(number)