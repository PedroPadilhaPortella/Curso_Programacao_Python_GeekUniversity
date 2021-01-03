last = int(input("Numero: "))

for i in range(last, -1, -1):
    if(i % 2 == 0):
        print("{}".format(i), end=', ')