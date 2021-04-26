palavrasProibidas = {"futebol", "politica", "sexo"}
frases = ["eu gosto de futebol e politica", "sexo é bom", "vamos a praia"]

for frase in frases:
    intersecao = palavrasProibidas.intersection(set(frase.lower().split()))
    if(intersecao):
        print(f"O texto possui palavras proibidas: {intersecao}")
    else:
        print("Texto autorizado: {}".format(frase))