def tipoTriangulo(a, b, c):
    canbe = canBeATriangle(a, b, c)
    if(canbe == True):
        if(a == b and b == c):
            return "Equilátero"
        elif(a == b or b == c or a == c):
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        print("Os lados não podem formar um triangulo!")
        exit()

def canBeATriangle(a, b, c):
    if(a >= b + c or b >= c + a or c >= a + b):
        return False
    else:
        return True


ladoa = float(input("Lado A: "))
ladob = float(input("Lado B: "))
ladoc = float(input("Lado C: "))
res = tipoTriangulo(ladoa, ladob, ladoc)
print("É um triangulo {}".format(res))