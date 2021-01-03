def fibonnaci(quantidade, sequencia = (0, 1)):
    return sequencia if(len(sequencia) == quantidade) else fibonnaci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == "__main__":
    resultado = fibonnaci(20)
    print(resultado)