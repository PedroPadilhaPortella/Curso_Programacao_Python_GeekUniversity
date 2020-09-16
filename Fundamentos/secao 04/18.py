def m3ToLitros(m3):
    litro = m3 * 1000
    print("{} metros cubicos são {:.2f} litros".format(m3, litro))

m3 = float(input("Quantos metros Cubicos? "))
m3ToLitros(m3)