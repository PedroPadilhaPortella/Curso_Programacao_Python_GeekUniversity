def metrosToAcres(metros):
    return metros * 0.000247

metros = float(input("Quantos metros quadrados? " ))
print("{:.0f} m2 são {:.2f} acres".format(metros, metrosToAcres(metros)))