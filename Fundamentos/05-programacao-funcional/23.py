def print_asteriscos(quantidade):
    asterisco = ''
    for i in range(0, quantidade):
        asterisco += '*'
        print(asterisco)
    
    for i in range(quantidade, 1, -1):
        asterisco = asterisco[:-1]
        print(asterisco)


n = int(input("Quantas asteriscos serão apresentadas: "))
print_asteriscos(n)