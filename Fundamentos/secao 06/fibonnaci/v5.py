def fibonnaci(quantidade, sequencia = (0, 1)):
    if (len(sequencia) == quantidade):
        return sequencia
    return fibonnaci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == "__main__":
    resultado = fibonnaci(12)
    print(resultado)