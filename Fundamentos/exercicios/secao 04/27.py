def HectaresToMetros(hectar):
    return hectar * 10000

hectar = float(input("Quantos hectares? " ))
print("{:.0f} hectares são {:.2f} m2".format(hectar, HectaresToMetros(hectar)))