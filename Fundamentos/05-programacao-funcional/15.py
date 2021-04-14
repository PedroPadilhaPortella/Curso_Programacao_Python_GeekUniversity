def get_lados_triangulo():
    lados = list()
    l1 = int(input("Lado 1: "))
    l2 = int(input("Lado 2: "))
    l3 = int(input("Lado 3: "))
    if(l1 < 0 or l2 < 0 or l3 < 0):
        raise Exception("All the sides must be greater than zero.")
    lados.append([l1, l2, l3])
    return lados[0]


def lados_formam_um_triangulo(lados):
    if(lados[0] + lados[1] > lados[2] and lados[1] + lados[2] > lados[0] and lados[0] + lados[2] > lados[1]):
        print('Os lados formam um triangulo!')
        return True
    else:
        print('Os lados não formam um triangulo!')
        return False


def get_tipo_triangulo(lados):
    if(lados[0] == lados[1] and lados[1] == lados[2]):
        return "Equilátero"
    elif(lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]):
        return "Isósceles"
    else:
        return "Escaleno"


def definir_tipo_triangulo():
    lados = get_lados_triangulo()
    triangulo = lados_formam_um_triangulo(lados)
    if(triangulo):
        retorno = dict()
        tipo = get_tipo_triangulo(lados)
        retorno['tipo'] = tipo
        retorno['lados'] = lados
        return retorno


resultado = definir_tipo_triangulo()
print(f"O tipo deste triangulo é {resultado['tipo']}, sendo seus lados {resultado['lados']}")