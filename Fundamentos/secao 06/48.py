def fibonnaci():
    fib = 0
    anterior = 0
    numeros = []
    while(fib < 4000000):
        if(fib % 2 == 0):
            numeros.append(fib)
        fib += anterior
        anterior = fib - anterior
        if(fib == 0):
            fib += 1
    return numeros

valores = fibonnaci()
print("Array de Fibonnaci dos valores pares até 4.000.000:")
print(valores)