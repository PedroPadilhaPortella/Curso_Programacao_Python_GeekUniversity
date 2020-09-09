from math import pow

def area(l):
    return pow(l, 2)

lado = float(input("Lado do quadrado: "))
print("A area do quadrado de lado {} é {}".format(lado, area(lado)))