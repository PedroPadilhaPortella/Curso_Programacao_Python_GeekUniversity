import re


def media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4

n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))
n3 = float(input("Nota 3:"))
n4 = float(input("Nota 4:"))
media = media(n1, n2, n3, n4)
print("A media das notas é {}".format(media))