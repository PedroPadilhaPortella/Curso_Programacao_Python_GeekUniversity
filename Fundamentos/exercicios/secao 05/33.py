def corretagem(oldPrice):
    newPrice = 0
    if(oldPrice <= 50):
        newPrice = oldPrice * 1.05
    elif(oldPrice > 50 and oldPrice <= 100):
        newPrice = oldPrice * 1.1
    elif(oldPrice > 100):
        newPrice = oldPrice * 1.15
    print("Novo Preço: R${:.2f}".format(newPrice))

    if(newPrice < 80):
        print("Barato")
    elif(newPrice >= 80 and newPrice <= 120):
        print("Normal")
    elif(newPrice >= 120 and newPrice <= 200):
        print("Caro")
    elif(newPrice > 200):
        print("Muito Caro")

preco = float(input("Preço Atual:"))
corretagem(preco)
