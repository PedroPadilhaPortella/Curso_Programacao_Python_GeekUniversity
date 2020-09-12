def aposentadoria(age, work):
    if(age >= 65 or work >= 30 or age >= 60 and work >= 25):
        print("Pode se Aposentar!")
    else:
        print("Não pode se Aposentar!")


age = int(input("Quantos anos?"))
work = int(input("Quantos anos de trabalho?"))
aposentadoria(age, work)