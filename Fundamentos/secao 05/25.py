from math import pow

def bhaskara():
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))

    if(a == 0):
        print('A não pode ser 0!')
        exit()
    
    delta = pow(b, 2) - (4 * a * c)
    if(delta < 0):
        print("Não existem raizes reais para essa equaçao")
        exit()
    elif(delta == 0):
        x =  (-b + delta) / (2 * a)
        print("A raiz é {}".format(x))
    else:
        x1 =  (-b + delta) / (2 * a)
        x2 =  (-b - delta) / (2 * a)
        print("As raizes são {} e {}".format(x1, x2))

bhaskara()
