def polegadasToCentimetros(polegadas):
    cms = polegadas * 2.54
    print("{} polegadas são {}cm".format(polegadas, cms))

pol = float(input("Quantas Polegadas? "))
polegadasToCentimetros(pol)