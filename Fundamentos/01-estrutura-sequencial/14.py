def grausToRadianos(grau):
    radiano = grau / 180
    print("{}° são {} pi radianos".format(grau, radiano))

grau = float(input("Quantos graus? "))
grausToRadianos(grau)