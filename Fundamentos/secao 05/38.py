dia = int(input("Dia:"))
mes = int(input("Mes:"))
ano = int(input("Ano:"))

validar = ''

if(ano <= 2020):
    if(mes == 2):
        if(dia > 0 and dia <= 28):
            validar = 'Válida'
        elif(dia > 0 and dia <= 29 and ano % 4 == 0):
            validar = 'Válida'
        else:
            validar = 'Inválida'
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if(dia > 0 and dia <= 30):
            validar = 'Válida'
        else:
            validar = 'Inválida'
    elif(mes <= 12 and mes > 0):
        if(dia > 0 and dia <= 31):
            validar = 'Válida'
        else:
            validar = 'Inválida'
    else:
        validar = 'Inválida'
else:
    validar = 'Inválida'

print(f"Essa data é {validar}")

