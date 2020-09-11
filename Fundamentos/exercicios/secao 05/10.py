def pesoIdeal(sexo, altura):
    if(sexo.lower() == "masculino"):
        return (altura * 72.7) - 58
    elif(sexo.lower() == "feminino"):
        return (altura * 62.1) - 44.7
    else:
        print("Sexo Inválido")
        exit()


nome = input("Nome: ")
sexo = input("Sexo: ")
altura = float(input("Altura: "))
peso = pesoIdeal(sexo, altura)
print("Seu peso ideal é {}".format(peso))