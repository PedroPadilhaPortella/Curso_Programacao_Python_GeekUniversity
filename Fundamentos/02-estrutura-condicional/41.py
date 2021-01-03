def imc(altura, peso):
    imc = peso / (altura ** 2)
    print("IMC: {:.2f}".format(imc))
    if(imc < 18.5):
        print("Abaixo do peso")
    elif(imc > 18.5 and imc < 24.9):
        print("Saudavel")
    elif(imc > 24.9 and imc < 29.9):
        print("Peso em excesso")
    elif(imc > 29.9 and imc < 34.9):
        print("Obesidade Grau 1")
    elif(imc > 34.9 and imc < 39.9):
        print("Obesidade Grau 2")
    elif(imc > 39.9):
        print("Obesidade Grau 3")

peso = float(input("Qual seu peso? "))
altura = float(input("Qual sua altura? "))
imc(altura, peso)