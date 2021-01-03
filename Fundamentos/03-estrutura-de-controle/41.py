def calcularResistencia(r1, r2):
    try:
        return (r1 * r2) / (r1 + r2)
    except:
        print("Base não pode ser nula")
        return 0

r= 1
while(r != 0):
    r1 = float(input("R1:"))
    r2 = float(input("R2:"))
    r = calcularResistencia(r1, r2)
    print(f"Resistencia = {r} Ohm")
