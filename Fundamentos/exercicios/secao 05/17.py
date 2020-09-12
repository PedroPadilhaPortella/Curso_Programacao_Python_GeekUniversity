def trapezio(maior,menor, h):
    if(maior <= 0 or menor <= 0 or h <= 0):
        print("Trapézio com medidas Inválidas")
    else:
        return (maior + menor) * h / 2


maior = float(input("Base maior: "))
menor = float(input("Base menor: "))
altura = float(input("Altura: "))
area = trapezio(maior, menor, altura)
print("Area do trapézio: {}".format(area))