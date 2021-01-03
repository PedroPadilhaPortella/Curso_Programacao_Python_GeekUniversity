def comanda():
    codigo = int(input("Codigo do produto: "))
    total = 0
    if(codigo == 100):
        total += 1.2
    elif(codigo == 101):
        total += 1.3
    elif(codigo == 102):
        total += 1.5
    elif(codigo == 103):
        total += 1.2
    elif(codigo == 104):
        total += 1.7
    elif(codigo == 105):
        total += 2.2
    elif(codigo == 106):
        total += 1
    else:
        print("Produto não especificado!")
    return total

def menu():
    print(f"Produto {'-'*10}  Codigo - Preço\nCachorro Quente    100  R$1.20\nBauru Simples      101  R$1.30\nBauru com Ovo      102  R$1.50\nHamburguer         103  R$1.20\nXburguer           104  R$1.70\nSuco               105  R$2.20\nRefrigerante       106  R$1.00")
    total = 0
    elementos = int(input("Quantos produtos serão comprados?"))
    for i in range(0, elementos):
        total += comanda()
    print("Total: R${:.2f}".format(total))

menu()