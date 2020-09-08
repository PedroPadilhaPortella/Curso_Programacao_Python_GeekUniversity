def metrosToHectares(metros):
    return metros * 0.0001

metros = float(input("Quantos metros quadrados? " ))
print("{:.0f} m2 são {} hectares".format(metros, metrosToHectares(metros)))