def maior(a, b):
    if(a > b):
        return a
    elif(b > a):
        return b
    else:
        print("O valores são iguais!")
        exit()


a = int(input("Valor 1:"))
b = int(input("Valor 2:"))

print(f"O maior valor é {maior(a, b)}")