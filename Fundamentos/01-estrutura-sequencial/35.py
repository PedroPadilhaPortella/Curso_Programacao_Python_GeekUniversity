from math import hypot

def hipotenusa(co, ca):
    return hypot(co, ca)

co = float(input("Cateto Oposto: "))
ca = float(input("Cateto Adjacente: "))
hip = hipotenusa(co, ca)
print("A hipotenusa de {} e {} é {}".format(co, ca, hip))