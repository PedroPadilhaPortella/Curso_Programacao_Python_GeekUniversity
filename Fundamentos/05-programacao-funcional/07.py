def celcius_to_fahrenheit(celcius):
    fahrenheit = celcius * (9/5) + 32
    return round(fahrenheit, 2)


def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit -32) * (5/9)
    return round(celcius,)


def converter_temperatura():
    opcao = int(input("Converter\n(1) Celcius para Fahrenheit\n(2) Fahrenheit para Celcius\n_"))
    valor = float(input("Qual o valor a ser convertido: "))
    if(opcao == 1):
        print(f"A temperatura de {valor}°C é de {celcius_to_fahrenheit(valor)}°F")
    elif(opcao == 2):
        print(f"A temperatura de {valor}°F é de {fahrenheit_to_celcius(valor)}°C")
    else:
        print("Opcao Inválida.")


converter_temperatura()