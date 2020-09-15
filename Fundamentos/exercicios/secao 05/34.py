def conceituar(nota, faltas):
    if(faltas <= 20):
        if(nota >= 9):
            print("A")
        elif(nota >= 7.5):
            print("B")
        elif(nota >= 5):
            print("C")
        elif(nota >= 4):
            print("D")
        elif(nota >= 0):
            print("E")
    
    elif(faltas > 20):
        if(nota >= 9):
            print("B")
        elif(nota >= 7.5):
            print("C")
        elif(nota >= 5):
            print("D")
        elif(nota >= 4):
            print("E")
        elif(nota >= 0):
            print("F")


nota = float(input("Nota:"))
faltas = int(input("Faltas:"))
conceituar(nota, faltas)