array = []
i = 0
while(i <= 15):
    n = int(input(f"Digite o {i}° valor: "))
    if(n in array):
        print("Esse valor é repetido, digite outro valor!")
    else:
        array.append(n)
        i += 1

print(array)