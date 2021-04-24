def potenciar(x, z):
    pow = x
    for i in range(1, z):
        pow *= x
    return pow


print(potenciar(2, 2))
print(potenciar(3, 3))
print(potenciar(10, 3))