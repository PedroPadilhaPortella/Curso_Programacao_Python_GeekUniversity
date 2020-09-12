from datetime import date


def bissexto(ano):
    if(ano == 0):
        ano = date.today().year
    print("O ano de {}".format(ano), end="")
    if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
        return 'é bissexto!'
    else:
        return 'não é bissexto!'


ano = int(input('Insira um ano para saber se ele é bissexto: '))
print(" {}".format(bissexto(ano)))