def jardasToMeters(jd):
    return jd * 0.91

jd = float(input("Distancia em Jardas: "))
print("A distancia de {} jardas são {} metros".format(jd, jardasToMeters(jd)))