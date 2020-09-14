def classificar(altura, peso):
    classe = 'none'
    if(altura < 1.2 and peso < 60):
        classe = 'A'
    elif((altura >= 1.2 and altura <= 1.7) and peso < 60):
        classe = 'B'
    elif(altura > 1.7 and peso < 60):
        classe = 'C'
    
    elif(altura < 1.2 and (peso >= 60 and peso <= 90)):
        classe = 'D'
    elif((altura >= 1.2 and altura <= 1.7) and (peso >= 60 and peso <= 90)):
        classe = 'E'
    elif(altura > 1.7 and (peso >= 60 and peso <= 90)):
        classe = 'F'
    
    elif(altura < 1.2 and peso > 90):
        classe = 'G'
    elif((altura >= 1.2 and altura <= 1.7) and peso > 90):
        classe = 'H'
    elif(altura > 1.7 and peso > 90):
        classe = 'I'
    return classe


altura = float(input("Qual a sua altura?"))
peso = float(input("Qual a seu Peso?"))

classe = classificar(altura, peso)
print("Sua classe é {}".format(classe))