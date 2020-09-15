dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

if(dia in range(1, 31) and mes in range(1, 13)):
    if(ano % 4 != 0 and mes == 2 and dia == 29):
        print("Data Inválida, ano Não Bissexto")
    else:
        print('Data Válida')
else:
    print("Data Inválida")