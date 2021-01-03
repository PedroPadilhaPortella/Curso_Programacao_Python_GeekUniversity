def calcularAlturaEscada(alturaDegrau, alturaDesejada):
    degraus = alturaDesejada / (alturaDegrau * 0.01)
    return degraus


alturaDesejada = float(input("Qual a altura desejada a alcançar, em metros? "))
alturaDegrau = float(input("Qual a altura de cada degrau, em centimetros? "))
degraus = calcularAlturaEscada(alturaDegrau, alturaDesejada)

print("Serão necessários {:.0f} degraus para alcançar a altura de {} mts".format(degraus, alturaDesejada))