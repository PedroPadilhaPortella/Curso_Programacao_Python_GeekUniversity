def litrosToM3(litro):
    m3 = litro / 1000
    print("{} litros são {:.2f}m3".format(litro, m3))

litro = float(input("Quantos Litros? "))
litrosToM3(litro)