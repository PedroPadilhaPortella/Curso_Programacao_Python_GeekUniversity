def converterMihasToQuilometros(quilometro):
    milha = quilometro / 1.61
    print("{} quilometros é igual a {} milhas".format(quilometro, milha))

quilometro = float(input("Qual a distancia em quilometros? "))
converterMihasToQuilometros(quilometro)