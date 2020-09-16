def divisivelPor3e5(n):
    if(n % 3 == 0 and n % 5 != 0 or n % 3 != 0 and n % 5 == 0):
        print("Divisivel por 5 ou 3")
    elif(n % 3 == 0 & n % 5 == 0):
        print("Divisivel por 3 e 5")
    else:
        print("Não é divisivel por 5 ou 3")


n = int(input("Numero: "))
divisivelPor3e5(n)