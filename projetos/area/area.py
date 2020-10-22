palavrasProibidas = {"futebol", "politica", "sexo"}
frases = ["eu gosto de futebol e politica", "sexo é bom", "vamos a praia"]

for frase in frases:
    inteersecao = palavrasProibidas.intersection(set(frase.lower().split()))
    if(inteersecao):
        print(f"O texto possui palavras proibidas: {inteersecao}")
    else:
        print("Texto autorizado: {}".format(frase))