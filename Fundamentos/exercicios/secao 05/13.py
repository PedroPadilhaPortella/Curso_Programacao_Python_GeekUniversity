def media(n1, n2, n3):
    return ((n1) + (n2) + (n3 * 2)) / 4


n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

print("Media: {}".format(media(n1, n2, n3)))