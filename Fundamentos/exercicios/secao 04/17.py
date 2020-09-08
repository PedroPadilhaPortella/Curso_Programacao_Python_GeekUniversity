def CentimetrosToPolegadas(cms):
    polegadas = cms / 2.54
    print("{} polegadas são {}cm".format(cms, polegadas))

cms = float(input("Quantos Centimetros? "))
CentimetrosToPolegadas(cms)