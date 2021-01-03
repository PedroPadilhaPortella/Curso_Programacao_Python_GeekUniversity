def crescente():
    x = int(input("X:"))
    y = int(input("Y:"))
    z = int(input("Z:"))

    if(x > y):
        alt = x
        x = y
        y = alt
    if(x > z):
        alt = x
        x = z
        z = alt
    if(y > z):
        alt = y
        y = z
        z = alt
    print(f"{x}\n{y}\n{z}")

crescente()