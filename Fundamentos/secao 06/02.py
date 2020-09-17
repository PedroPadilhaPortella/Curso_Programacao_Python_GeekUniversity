print("For")
for i in range(1, 101):
    print("{},".format(i), end=' ')
print("\n\nWhile")
valor = 1
while(valor <= 100):
    print("{},".format(valor), end=' ')
    valor += 1

print("\n\nDo_While\n")
n = 1
while True:
    print("{},".format(n), end=' ')
    n += 1
    if(n > 100):
        break