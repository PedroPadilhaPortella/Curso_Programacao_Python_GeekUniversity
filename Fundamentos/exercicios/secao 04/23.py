def metersToJardas(mt):
    return mt / 0.91

mt = float(input("Distancia em Metros: "))
print("A distancia de {} mts são {:.2f} jardas".format(mt, metersToJardas(mt)))